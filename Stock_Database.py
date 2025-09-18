import requests
import pandas as pd
import pyodbc
import urllib3
from datetime import datetime

# 關閉 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# API URL 與參數
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY"
stock_code = "2330"
# 示範使用當前日期的月份
query_date = datetime.now().strftime("%Y%m%d") 
params = {
    "response": "json",
    "date": query_date,
    "stockNo": stock_code
}

try:
    # 抓取 JSON
    print(f"正在從台灣證券交易所抓取 {stock_code} 在 {query_date[:6]} 的股價資料...")
    response = requests.get(url, params=params, verify=False, timeout=10)
    response.raise_for_status()  # 如果請求失敗 (e.g., 404, 500)，會拋出異常
    data_json = response.json()

    if data_json["stat"] != "OK":
        print(f"抓取失敗: {data_json.get('stat')} - {data_json.get('message')}")
    else:
        print("資料抓取成功，正在進行處理...")
        # 轉成 DataFrame
        columns = data_json["fields"]
        data = data_json["data"]
        df = pd.DataFrame(data, columns=columns)

        # 民國年轉西元年
        def roc_to_ad(date_str):
            parts = date_str.split("/")
            year = int(parts[0]) + 1911
            return f"{year}-{parts[1]}-{parts[2]}"

        df["日期"] = df["日期"].apply(roc_to_ad)
        df['日期'] = pd.to_datetime(df['日期']).dt.date # 轉換為 date 物件

        # 數字清理
        for col in ["成交股數", "成交金額", "成交筆數"]:
            df[col] = df[col].str.replace(",", "").astype(int)

        for col in ["開盤價", "最高價", "最低價", "收盤價", "漲跌價差"]:
            # 將 '--' 這種無效值替換為 NaN，以便後續處理
            df[col] = df[col].astype(str).str.replace("X", "").str.replace(",", "").str.replace("--", "")
            df[col] = pd.to_numeric(df[col], errors="coerce")
        
        df = df.dropna() # 移除有缺失值的行
        print(f"資料清理完成，共 {len(df)} 筆有效交易日。")

        # --- 資料庫操作 ---
        print("準備連接資料庫並寫入資料...")
        conn = pyodbc.connect(
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=DESKTOP-17ILG44\SQLEXPRESS;' # 請替換成您自己的伺服器名稱
            r'DATABASE=Stock;'
            r'Trusted_Connection=yes;'
        )
        cursor = conn.cursor()

        # SQL MERGE 陳述式
        # 如果 TradeDate 和 StockCode 符合，則 UPDATE
        # 如果不符合，則 INSERT
        merge_sql = """
        MERGE INTO TSMC AS target
        USING (VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)) AS source (
            StockCode, TradeDate, Volume, Turnover, OpenPrice, 
            HighPrice, LowPrice, ClosePrice, Change, TradeCount
        )
        ON target.TradeDate = source.TradeDate AND target.StockCode = source.StockCode
        WHEN MATCHED THEN
            UPDATE SET
                Volume = source.Volume,
                Turnover = source.Turnover,
                OpenPrice = source.OpenPrice,
                HighPrice = source.HighPrice,
                LowPrice = source.LowPrice,
                ClosePrice = source.ClosePrice,
                Change = source.Change,
                TradeCount = source.TradeCount
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (
                StockCode, TradeDate, Volume, Turnover, OpenPrice, 
                HighPrice, LowPrice, ClosePrice, Change, TradeCount
            )
            VALUES (
                source.StockCode, source.TradeDate, source.Volume, source.Turnover, 
                source.OpenPrice, source.HighPrice, source.LowPrice, source.ClosePrice, 
                source.Change, source.TradeCount
            );
        """
        
        # 遍歷 DataFrame，執行 MERGE 操作
        for _, row in df.iterrows():
            cursor.execute(
                merge_sql,
                stock_code,
                row["日期"],
                row["成交股數"],
                row["成交金額"],
                row["開盤價"],
                row["最高價"],
                row["最低價"],
                row["收盤價"],
                row["漲跌價差"],
                row["成交筆數"]
            )

        conn.commit()
        cursor.close()
        conn.close()

        print(f"資料已成功同步至 Stock.TSMC (股票代號: {stock_code})")

except requests.exceptions.RequestException as e:
    print(f"網路請求失敗: {e}")
except pyodbc.Error as e:
    print(f"資料庫操作失敗: {e}")
except Exception as e:
    print(f"發生未預期的錯誤: {e}")