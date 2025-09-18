# 📌 TWSE 個股日成交資訊爬蟲與資料庫同步

> 自動抓取台灣證券交易所 (TWSE) 的個股日成交資料，清理後同步至 MS SQL Server 資料庫  
> 範例以 **台積電 (2330)** 為例，可擴展至多檔股票

![Version](https://img.shields.io/badge/version-1.0.0-green)
![Build](https://img.shields.io/badge/build-running-blue)

---

## 📖 專案簡介
本專案示範如何使用 Python + pandas + pyodbc 搭配 MS SQL Server：

- 自動抓取 TWSE 公開的股票日成交資訊 (JSON API)
- 清理、轉換資料格式 (含民國年轉西元年)
- 透過 SQL MERGE 指令寫入資料庫，避免重複插入

本範例以 台積電 (2330) 為例，適合需要 持續收集股價資料 的分析或投資應用。

---

## ✨ 功能特色
- 支援指定股票代碼
- 自動判斷當前月份，抓取對應期間資料
- 自動進行資料清理與型別轉換
- 透過 MERGE 同步至資料庫 (避免重複插入，若已存在則更新)
- 可擴展至多檔股票

---

## 📂 專案結構
```nginx
Stock_Database
├── Stock_Database.py    # 主程式，抓取 TWSE 股價並寫入資料庫
├── requirements.txt     # 套件需求
├── Stock.bacpac         # 資料庫的格式(以資料表 TSMC 為範例)
├── LICENSE              # LICENSE
└── README.md            # 專案說明文件
```

---

## 🚀 安裝與使用

### 1️⃣ 環境需求
- Python >= 3.9 (開發環境使用 3.13.6)
- MS SQL Server (建議 2017 以上)
- ODBC Driver 17 for SQL Server

安裝所需套件：
- requests
- pandas
- pyodbc

### 2️⃣ 安裝步驟

Step1. 下載專案
```bash
git clone https://github.com/Leiinori/Stock_Database.git
cd Stock_Database
```

Step2. 安裝套件 <br>
使用requirements.txt 安裝 :
```bash
pip install -r requirements.txt
```

手動安裝 : <br>
```bash
pip install requests pandas pyodbc
```

Step3. 建立資料庫與資料表
建立資料表 (MS SQL Server)，以建立 資料庫Stock & 建立 資料表TSMC 為範例 <br>
使用SQL指令建立 :
```sql
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

或是使用MS SQL Server操作介面匯入Stock.bacpac


### 3️⃣ 使用方式
Step1. 開啟主程式 Stock_Database.py，修改目標股票的代碼參數
```python
stock_code = "2330"  # 台積電
```

Step 2. 修改資料庫連線資訊
```python
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=你的伺服器名稱;'
    r'DATABASE=Stock;'
    r'Trusted_Connection=yes;'
)
```

Step 3. 修改資料表資訊，以台積電(TSMC)為例
```sql
MERGE INTO TSMC AS target
```

Step 4. 執行程式
```bash
python Stock_Database.py
```

Step 5. 範例輸出，以台積電(2330)為例
```yaml
正在從台灣證券交易所抓取 2330 在 202509 的股價資料...
資料抓取成功，正在進行處理...
資料清理完成，共 20 筆有效交易日。
資料已成功同步至 Stock.TSMC (股票代號: 2330)
```

---

## 🔗 參考

- [TWSE API](https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html)
- [pandas 官方文件](https://pandas.pydata.org/docs/)
- [pyodbc 官方文件](https://github.com/mkleehammer/pyodbc)

---

## 📌 開發計劃
✅ 已完成 <br>
- 抓取單檔股票資料並存入資料庫 <br>
- 自動判斷當月日期 <br>
- SQL MERGE 同步避免重複

🚧 計劃中 <br>
- 支援多股票批次匯入 <br>
- 加入排程 (每日自動抓取) <br>

---

## 📜 授權

本專案採用 [MIT License](LICENSE)


---

## 👤 作者

[Ming Lei (Git Hub)](https://github.com/Leiinori)

---
