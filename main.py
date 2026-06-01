import os
import telebot
import time

TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TOKEN)
TARGET_ID = "@Ai1t_src1Bot" 

BASE_URL = "https://t.me/pw_neev_2025_26/"
link_number = 4475

while True:
    bot.send_message(TARGET_ID, f"{BASE_URL}{link_number}")
    link_number += 1
    time.sleep(300) # 5 minutes
