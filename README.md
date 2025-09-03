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
git clone https://github.com/ankitmishra42/TelegramBotAutomation.git
cd TelegramBotAutomation
```bash

###2️⃣ Install dependencies
```bash
pip install requests mysql-connector-python python-telegram-bot
bash```

###3️⃣ Configure environment variables

Update your bot credentials and DB settings inside the script (TelegramBot.py):
```python
BOT_TOKEN = "your-telegram-bot-token"
CHAT_ID = "your-chat-id"
API_KEY = "your-dextools-api-key"

mydb = mysql.connector.connect(
  host="localhost",
  user="your-db-user",
  password="your-db-password",
  database="your-db-name"
)
python```

###4️⃣ Setup MySQL Database

Run the following SQL commands:

CREATE DATABASE systemicAltruism2;

USE systemicAltruism2;

CREATE TABLE newdata2 (
  id INT AUTO_INCREMENT PRIMARY KEY,
  data JSON,
  dateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


###5️⃣ Run the bot
python TelegramBot.py

---

##📲 How It Works

Script fetches data from DEXTools API every 10 seconds.
Inserts the new data into MySQL (newdata2 table).
Checks if there are new records in the last 12 seconds.
If yes, sends a Telegram alert with the new data.

---

##📌 Example Alert
New Data Detected: {'id': 101, 'data': {...}, 'dateTime': '2025-09-03 15:45:10'}

---

##🚧 Future Improvements

Add Docker support for easy deployment.
Add logging for debugging.
Implement error handling & retries for API calls.
Extend to multiple APIs & multiple bot channels.
