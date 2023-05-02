# Posting photos in telegram channel
The program accepts from the user the path to the folder with photos, the file name of the photo and using the telegram bot publishes this photo in the telegram channel. If the user has not specified the name of the photo file, the program will randomly select the photo itself and publish it.
## How to install

How to register a bot - [click here](https://way23.ru/регистрация-бота-в-telegram.html)
- [BotFather](https://telegram.me/BotFather)
  - /start
  - /newbot
- How to create a channel, bot and get a token - [click here](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
- Bypass Telegram blocking - [click here](https://bigpicture.ru/kak-obojti-blokirovku-telegram-na-smartfone-desktope-i-v-brauzere/)

#### Requirements

Python3 should be already installed. Then use pip to install dependencies:
Specify your folder name where the downloaded photos will be saved
```
pip install -r requirements.txt
```
### Create an environment

#### Environment variables

- TELEGRAM_BOT_TOKEN

1. Place the `.env` file in the root folder of your project.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:
```
$ cat .env
TELEGRAM_BOT_TOKEN=1a5d754733b01560143c90238efa4esad1taec48
```
## Example of running a script
- Launching a program for publishing photos:
```
C:\Users\telegram_project> python telegram_photo.py -p C:/Users/Вячеслав/Desktop/Учеба/telegram_project/space_photos/ -f spacex_1.jpg
Photo spacex_1.jpg uploaded
C:\Users\telegram_project> python telegram_photo.py -p C:/Users/Вячеслав/Desktop/Учеба/telegram_project/space_photos/
Photo photos_epic_1b_20230421002712.png uploaded
```
## Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org.](https://dvmn.org/)