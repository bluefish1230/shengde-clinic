# 盛德整復所 - 靜態網站

這是盛德整復所的完整靜態網站版本，可以直接在任何網頁伺服器上運行。

## 📁 檔案結構

```
shengde-static/
├── index.html          # 主要 HTML 檔案（包含所有頁面）
├── assets/             # CSS 和 JavaScript 檔案
│   ├── index-*.css     # 樣式表
│   └── index-*.js      # JavaScript 程式碼
└── README.md           # 本檔案
```

## 🚀 快速開始

### 方式 1：使用 Python 簡易伺服器（推薦）

```bash
# Python 3
python3 -m http.server 8000

# 然後在瀏覽器中打開：http://localhost:8000
```

### 方式 2：使用 Node.js http-server

```bash
# 全域安裝 http-server
npm install -g http-server

# 在本目錄執行
http-server

# 然後在瀏覽器中打開：http://localhost:8080
```

### 方式 3：使用 Live Server（VS Code 擴充功能）

1. 在 VS Code 中安裝 "Live Server" 擴充功能
2. 右鍵點擊 `index.html`
3. 選擇 "Open with Live Server"

### 方式 4：直接上傳到網頁伺服器

1. 將所有檔案上傳到您的網頁伺服器（如 Netlify、Vercel、GitHub Pages 等）
2. 設定根目錄指向本資料夾
3. 訪問您的網域即可

## 📄 頁面內容

網站包含以下頁面：

- **首頁** - 盛德整復所介紹和服務概況
- **關於盛德** - 詳細的服務說明和專精領域
- **收費標準** - 初診和回診的收費方案
- **聯絡我們** - 地址、電話、LINE 預約資訊
- **患者管理** - 患者資料管理（需要後端支援，此版本已移除）

## ⚙️ 技術細節

- **前端框架**：React 19 + TypeScript
- **樣式**：Tailwind CSS 4
- **字體**：Google Fonts (Noto Serif TC, Noto Sans TC)
- **打包工具**：Vite

## 📝 修改網站內容

如果您想修改網站內容（如地址、電話等），您需要：

1. 下載完整源代碼版本
2. 修改相應的 React 組件檔案
3. 執行 `pnpm build` 重新構建
4. 使用新生成的 `dist/public` 檔案

## 🔒 注意事項

- 此版本是純靜態網站，不包含後端功能
- 患者管理功能已移除
- 所有頁面導航都是客戶端路由，無需伺服器支援

## 📞 支援

如有任何問題或需要修改，請聯絡我們。

---

**盛德整復所**
地址：411臺中市太平區育仁路171號
電話：0915 231 233
預約 LINE：goodlife0326
