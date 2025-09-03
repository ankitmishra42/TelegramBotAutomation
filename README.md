# 🚀 Telegram Bot for API Monitoring & Database Alerts  

This project is a **Telegram bot automation** that:  
- Fetches token data from the **DEXTools API**.  
- Stores the fetched data in a **MySQL database**.  
- Monitors the database for **new entries/changes**.  
- Sends **real-time alerts** to a Telegram group/channel when new data is detected.  

---

## 📌 Features  
- Fetch data from DEXTools API.  
- Store API responses in MySQL.  
- Monitor database changes in real-time.  
- Send alerts via **Telegram Bot** automatically.  
- Runs continuously using **asyncio**.  

---

## 🛠️ Tech Stack  
- **Python**: asyncio, requests, json, mysql-connector  
- **Telegram Bot API** (`python-telegram-bot`)  
- **MySQL**: Data storage & change tracking  
- **DEXTools API**: Data source  

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/ankitmishra42/telegram-db-alert-bot.git
cd telegram-db-alert-bot
