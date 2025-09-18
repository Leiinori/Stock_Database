# 📌 個股日成交資訊爬蟲
> 從台灣證券所爬取個股日成交資訊，將資料匯入資料庫中

![Version](https://img.shields.io/badge/version-1.0.0-green)
![Build](https://img.shields.io/badge/build-running-blue)

---

## 📖 專案簡介
學習到Python爬蟲與資料庫的單元時，給自己的一個小專題題目作為練習，並記錄製作過程遇到的問題與解決方式。

本專案用於 **自動抓取台灣證券交易所 (TWSE) 的股價資料**，並將資料寫入 **MS SQL Server 資料庫**，主程式與資料庫以台積電(2330)為例子。

- 適用對象：收集股票資訊需求，並建立資料庫持續收集資料，用於分析或其他應用者
- 使用的程式語言：Python + MS SQL

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
├── Note                 # 編寫心得與註記 <br>
└── README.md            # 專案說明文件 <br>

---

## 🚀 安裝與使用

### 1️⃣ 環境需求
- Python (>=3.9)    # 開發所用的版本為3.13.6 <br>
- requests <br>
- pandas <br>
- pyodbc <br>

### 2️⃣ 安裝步驟
```bash
# 下載專案
git clone https://github.com/Leiinori/NH_Downloader.git

# 安裝依賴
pip install requests beautifulsoup4 Pillow

```

---

### 3️⃣ 使用方式
<<<步驟 1>>> <br>
安裝Python

<<<步驟 2>>> <br>
安裝所需的套件

<<<步驟 3>>> <br>
下載主程式檔nhentai_downloader.py

<<<步驟 4>>> <br>
編譯執行程式，輸入對應的6碼開始下載

---

## 📌 開發計劃
 <<<已完成的功能>>> <br>
- 輸入對應的6碼即可開始下載 <br>
- 下載的圖片依序進行編號與轉成jpg檔 <br>

 <<<計劃中的功能>>> <br>
- 想辦法解決反爬蟲的機制 (2025/08/12測試發現網站有反爬蟲機制，7月時還未有) <br>
- 打包成exe執行檔，省去使用者前置所需安裝的步驟 <br>
- 圖像UI操作介面，輸入6碼後先顯示作品名稱預覽，確認無誤後再進行下載 <br>

