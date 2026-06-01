import os
import telebot
import time

TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TOKEN)
TARGET_ID = "-1003926389516" 
BASE_URL = "https://t.me/pw_neev_2025_26/"

# File se last number padhein
def get_last_number():
    if os.path.exists("number.txt"):
        with open("number.txt", "r") as f:
            return int(f.read().strip())
    return 4475 # Default start

while True:
    link_number = get_last_number()
    
    # Message bhejen
    try:
        bot.send_message(TARGET_ID, f"{BASE_URL}{link_number}")
        
        # Number update karke save karein
        with open("number.txt", "w") as f:
            f.write(str(link_number + 1))
            
    except Exception as e:
        print(f"Error: {e}")
        
    time.sleep(300) # 5 minutes
