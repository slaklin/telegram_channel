import os

import telegram
from dotenv import load_dotenv

load_dotenv()
tg_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=tg_bot_token)
bot.send_message(chat_id='@cosmic_life1990', text="Welcome to our channel")