import argparse
import os
import random

import telegram
from dotenv import load_dotenv


def publish_image_telegram(tg_bot_token, file_name, path, chat_id):
    bot = telegram.Bot(token=tg_bot_token)
    if file_name:
        with open(f'{path}{file_name}', 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
            print(f'Photo {file_name} uploaded')
    else:
        random_name = random.choice(os.listdir(path))
        with open(f'{path}{random_name}', 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
            print(f'Photo {random_name} uploaded')


def main():
    load_dotenv()
    tg_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    parser = argparse.ArgumentParser('Sending a photo to the telegram channel')
    parser.add_argument('--path', '-p', help='The path to the folder with photos')
    parser.add_argument('--file_name', '-f', help='Photo file name')
    user_parameters = parser.parse_args()
    file_name = user_parameters.file_name
    path = user_parameters.path
    publish_image_telegram(tg_bot_token, file_name, path, chat_id)


if __name__ == "__main__":
    main()
