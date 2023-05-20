import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def publish_photos_telegram(bot, number_of_hours, chat_id):
    path_photo = './space_photos'
    directory = os.walk(path_photo)
    photos_from_directory = next(directory)[2]
    while True:
        random.shuffle(photos_from_directory)
        for photo in photos_from_directory:
            with open(f'./space_photos/{photo}', 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
                print(f'Photo {photo} uploaded')
                time.sleep(number_of_hours * 3600)


def main():
    load_dotenv()
    tg_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    bot = telegram.Bot(token=tg_bot_token)
    parser = argparse.ArgumentParser('Program Description')
    parser.add_argument('freq', default=4, type=int, help='Frequency of publication of photos (in hours)')
    args = parser.parse_args()
    number_of_hours = args.freq
    publish_photos_telegram(bot, number_of_hours, chat_id)


if __name__ == "__main__":
    main()
