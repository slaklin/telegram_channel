# Posting photos in telegram channel
The program takes a time interval (in hours) from the user and, taking into account it, publishes photos in the telegram channel.

## How to install
In the code, you must explicitly specify the folder from where the program will publish photos.

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
TELEGRAM_BOT_TOKEN=1a5d754733b01560143c70238efa4esad1taec48
```
## Example of running a script
- Launching a program for publishing photos:
```
C:\Users\telegram_project> python telegram_bot.py 4
Photo apod_photos_1.jpg uploaded
Photo photos_epic_1b_20230421002712.png uploaded
Photo spacex_1.jpg uploaded
```

## Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org.](https://dvmn.org/)