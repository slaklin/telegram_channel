import argparse
import os
import random

import telegram
from dotenv import load_dotenv


def publish_image_telegram(bot, user_parameters):
    if user_parameters.file_name:
        path = user_parameters.path
        bot.send_document(chat_id='@cosmic_life1990', document=open(f'{path}{user_parameters.file_name}', 'rb'))
        print(f'Photo {user_parameters.file_name} uploaded')
    else:
        file_name = random.choice(os.listdir(user_parameters.path))
        path = user_parameters.path
        bot.send_document(chat_id='@cosmic_life1990', document=open(f'{path}{file_name}', 'rb'))
        print(f'Photo {file_name} uploaded')


def main():
    load_dotenv()
    tg_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = telegram.Bot(token=tg_bot_token)
    parser = argparse.ArgumentParser('Sending a photo to the telegram channel')
    parser.add_argument('--path', '-p', help='The path to the folder with photos')
    parser.add_argument('--file_name', '-f', help='Photo file name')
    user_parameters = parser.parse_args()
    publish_image_telegram(bot, user_parameters)


if __name__ == "__main__":
    main()
