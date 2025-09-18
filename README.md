# 📌 個股日成交資訊爬蟲
> 從台灣證券所爬取個股日成交資訊，將資料匯入資料庫中

![Version](https://img.shields.io/badge/version-1.0.0-green)
![Build](https://img.shields.io/badge/build-running-blue)

---

## 📖 專案簡介
學習到Python爬蟲與資料庫的單元時，給自己的一個小專題題目作為練習，並記錄製作過程遇到的問題與解決方式。

本專案用於 **自動抓取台灣證券交易所 (TWSE) 的股價資料**，並將資料寫入 **MS SQL Server 資料庫**，主程式與資料庫以台積電(2330)為例子。

- 適用對象：收集股票資訊需求，並建立資料庫持續收集資料，用於分析或其他應用者
- 使用的程式語言：Python + MS SQL Server

---

## ✨ 功能特色
- 輸入所要查詢的股票代碼
- 自動辨識當前時間的月份，並抓取該股票對應月份的資訊
- 抓取成功後匯入資料庫的資料表中(需預先建立好資料庫與資料表)

---

## 📂 專案結構
<<<Stock_Database>>> <br>
├── Stock_Database.py    # 主程式，抓取 TWSE 股價並寫入資料庫 <br>
├── requirements.txt     # 套件需求 <br>
├── Stock.bacpac         # 資料庫的格式(以資料表 TSMC 為範例) <br>
└── README.md            # 專案說明文件 <br>

---

## 🚀 安裝與使用

### 1️⃣ 環境需求
- Python (>=3.9)    # 開發所用的版本為3.13.6 <br>
- requests <br>
- pandas <br>
- pyodbc <br>

### 2️⃣ 安裝步驟

2-1. 下載專案
```bash
git clone https://github.com/Leiinori/Stock_Database.git
```

2-2. 安裝套件(使用requirements.txt)
```bash
pip install -r requirements.txt
```

2-2. 安裝套件(手動)
```bash
pip install requests pandas pyodbc
```

2-3. 建立資料表 (MS SQL Server)，以建立 資料庫Stock & 建立 資料表TSMC 為範例
```bash
-- 建立資料庫 (若不存在)
IF NOT EXISTS (
    SELECT name FROM sys.databases WHERE name = N'Stock'
)
BEGIN
    CREATE DATABASE Stock;
END
GO

-- 切換至 Stock 資料庫
USE Stock;
GO

-- 建立資料表 TSMC
IF OBJECT_ID('TSMC', 'U') IS NULL
BEGIN
    CREATE TABLE TSMC (
        StockCode   VARCHAR(10) NOT NULL,
        TradeDate   DATE NOT NULL,
        Volume      BIGINT,
        Turnover    BIGINT,
        OpenPrice   DECIMAL(10,2),
        HighPrice   DECIMAL(10,2),
        LowPrice    DECIMAL(10,2),
        ClosePrice  DECIMAL(10,2),
        Change      DECIMAL(10,2),
        TradeCount  INT,
        CONSTRAINT PK_TSMC PRIMARY KEY (StockCode, TradeDate)
    );
END
GO
```
2-3. 建立資料表 (匯入Stock.bacpac)

### 3️⃣ 使用方式
<<<步驟 1>>> <br>
開啟Stock_Database.py

<<<步驟 2>>> <br>
輸出想查詢的股票代碼，這裡是以台積電(2330)為例
```bash
stock_code = "2330"
```

<<<步驟 3>>> <br>
修改MS SQL Sever對應參數
```bash
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=你的伺服器名稱;'
    r'DATABASE=Stock;'
    r'Trusted_Connection=yes;'
)
```

<<<步驟 4>>> <br>
若建立其他股票的資料表，修改對應SQL語法 <br>
```bash
MERGE INTO 資料表名稱 AS target
```

<<<步驟 5>>> <br>
執行程式
```bash
python Stock2330.py
```

<<<範例輸出>>>
程式會在終端顯示處理進度，以台積電(2330)為例： <br>

正在從台灣證券交易所抓取 2330 在 202509 的股價資料... <br>
資料抓取成功，正在進行處理... <br>
資料清理完成，共 20 筆有效交易日。 <br>
資料已成功同步至 Stock.TSMC (股票代號: 2330) <br>

---

## 🔗 參考

- [TWSE API](https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html)
- [pandas 官方文件](https://pandas.pydata.org/docs/)
- [pyodbc 官方文件](https://github.com/mkleehammer/pyodbc)

---

## 📌 開發計劃
 <<<已完成的功能>>> <br>
- 自動辨識當前時間的月份，並抓取該股票對應月份的資訊 <br>
- 抓取成功後匯入資料庫的資料表中 <br>

 <<<計劃中的功能>>> <br>
- 加入排程功能，讓程式可以每天固定時間進行抓取並匯入資料表中 <br>

