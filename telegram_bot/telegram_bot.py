import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def publish_photos_telegram(bot, number_of_hours):
    path_photo = 'C:/Users/Вячеслав/Desktop/Учеба/telegram_project/space_photos'
    directory = os.walk(path_photo)
    photos_from_directory = next(directory)[2]
    while True:
        random.shuffle(photos_from_directory)
        for photo in photos_from_directory:
            bot.send_document(chat_id='@cosmic_life1990',
                              document=open(f'C:/Users/Вячеслав/Desktop/Учеба/telegram_project/space_photos/{photo}',
                                            'rb'))
            print(f'Photo {photo} uploaded')
            time.sleep(number_of_hours * 3600)


def main():
    load_dotenv()
    tg_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = telegram.Bot(token=tg_bot_token)
    parser = argparse.ArgumentParser('Program Description')
    parser.add_argument('freq', default=4, type=int, help='Frequency of publication of photos (in hours)')
    args = parser.parse_args()
    number_of_hours = args.freq
    publish_photos_telegram(bot, number_of_hours)


if __name__ == "__main__":
    main()
