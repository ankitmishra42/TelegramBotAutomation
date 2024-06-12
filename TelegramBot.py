# Importing modules
import requests
import asyncio
import json
import mysql.connector
from telegram import Bot

# Telegram bot token
BOT_TOKEN = "7108118406:AAHhGpOb8MK-EX4V9Eg_7zm11DE6lfgmtGM"
CHAT_ID = "-1002098677906"  # Your Telegram chat ID
                                  
# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Function to check for database changes
async def check_database_changes():
    
    # Replace 'YOUR_API_KEY' with your actual DEXTools API key
    API_KEY = "91dab760352da526cd92910714de4fd1"

    # Token
    endpoint_url = "https://api.dextools.io/v2/token/ether/0xfb7b4564402e5500db5bb6d63ae671302777c75a/info"

    # Construct the request headers with the API key
    headers = {'X-api-key': API_KEY}
    
    # Send the HTTP request to the API endpoint
    response = requests.get(endpoint_url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response data
        mdata = response.json()
        
        # Extrecting Data From Json file & Storing in variable
        user_data1 = mdata['data']
        
        # Parse the JSON response into string
        user_data = json.dumps(user_data1)
        
        
        # MySQL database consept Start
        # Create a connection to the database
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="systemicAltruism2"
        )

        
        # Create a cursor object
        mycursor = mydb.cursor()

        # Create an INSERT statement
        try:
            sql2 = "INSERT INTO `newdata2` (`data`) VALUES (%s);"

            # Execute the INSERT statement
            value = [user_data]
            mycursor.execute(sql2, value)
            
        except mysql.connector.IntegrityError:
            if False:
                print("The value you are trying to insert is already in the database.")
                
        # Commit the changes to the database
        mydb.commit()
        
        # Fetching Data From Database
        sql1 = "SELECT * FROM `newdata2` WHERE dateTime > NOW() - INTERVAL 12 SECOND"
        mycursor.execute(sql1)
        changes = mycursor.fetchall()
        if changes: 
            for change in changes:
                # Send notification to Telegram
                message = f"New Data Detected: {change}"
                await bot.send_message(chat_id=CHAT_ID, text=message)

        # Close the cursor object
        mycursor.close()
        
        # MySQL database consept End
           
    else:
        # Handle errors if the request was not successful
        await bot.send_message(chat_id=CHAT_ID, text="Error: "+str(response.status_code))

# Main function to continuously monitor the database
async def main():
    while True:
        await check_database_changes()
        # Adjust the sleep duration based on your requirements
        await asyncio.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
   asyncio.run(main())