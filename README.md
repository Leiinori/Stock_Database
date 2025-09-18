# 📌 個股日成交資訊爬蟲
> 從台灣證券所爬取個股日成交資訊，將資料匯入資料庫中

![Version](https://img.shields.io/badge/version-1.0.0-green)
![Build](https://img.shields.io/badge/build-running-blue)

---

## 📖 專案簡介
學習到Python爬蟲與資料庫的單元時，給自己的一個小專題題目作為練習，並記錄製作過程遇到的問題與解決方式。

使用台灣證券所提供的API查詢個股日成交資訊，並將資料做處理後，匯入資料庫中

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
├── Stock_Database.py # 主程式碼 <br>
├── Stock.bacpac # 資料庫的格式 <br>
├── Note # 編寫心得與註記 <br>
└── README.md <br>

Stock_Database/
├─ Stock2330.py           # 主程式，抓取 TWSE 股價並寫入資料庫
├─ requirements.txt       # 套件需求
├─ README.md              # 專案說明文件
├─ sql/
│   └─ create_tsmc.sql    # SQL 建表語法
└─ data/
    └─ sample.json        # 範例 API JSON 資料 (可選)


---

## 🚀 安裝與使用

### 1️⃣ 環境需求
- Python-3.13.6 # 開發所用的版本 <br>
- requests <br>
- beautifulsoup4 <br>
- Pillow <br>

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

