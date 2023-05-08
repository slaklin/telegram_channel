# Posting photos in telegram channel
This project provides scripts for downloading thematic images from various sites using API and automated publication of these images in the telegram channel

## How to install
1. Create [api.nasa.gov](https://api.nasa.gov/#epic) Generate API Key for work with API.

2. How to register a bot - [click here](https://way23.ru/регистрация-бота-в-telegram.html)
- [BotFather](https://telegram.me/BotFather)
  - /start
  - /newbot
- How to create a channel, bot and get a token - [click here](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
- Bypass Telegram blocking - [click here](https://bigpicture.ru/kak-obojti-blokirovku-telegram-na-smartfone-desktope-i-v-brauzere/)

#### Requirements

Python3 should be already installed. Then use pip to install dependencies:
```
pip install -r requirements.txt
```
### Create an environment

#### Environment variables

- TELEGRAM_BOT_TOKEN
- NASA_API_KEY

1. Place the `.env` file in the root folder of your project.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:

```
$ cat .env
TELEGRAM_BOT_TOKEN=1a5d754733b01560143c70238efa4esad1taec48
NASA_API_KEY=1a5d754733b01560143c70238efa4esad1taec48
```
## Example of running a script

#### This program accepts a time interval (in hours) from the user.
- Launching a program for publishing photos:
```
C:\Users\telegram_project> python telegram_bot.py 4
Photo apod_photos_1.jpg uploaded
Photo photos_epic_1b_20230421002712.png uploaded
Photo spacex_1.jpg uploaded
```
#### The program accepts from the user the path to the folder with photos and the file name of the photo.
- Launch the program to publish the desired photo:
```
C:\Users\telegram_project> python telegram_photo.py -p C:/Users/Вячеслав/Desktop/Учеба/telegram_project/space_photos/ -f spacex_1.jpg
Photo spacex_1.jpg uploaded
C:\Users\telegram_project> python telegram_photo.py -p C:/Users/Вячеслав/Desktop/Учеба/telegram_project/space_photos/
Photo photos_epic_1b_20230421002712.png uploaded
```
#### The program downloads the specified number of APOD photos.
- Launching the program to download photos:
```
C:\Users\telegram_project> python uploading_NASA_APOD_photos.py 3
Downloaded apod_photos_1.jpg
Downloaded apod_photos_2.jpg
Downloaded apod_photos_3.gif
```
#### The code takes the launch ID from the user and downloads all the photos of that moment.
- Launching the program to download photos:
```
C:\Users\telegram_project> python fetch_spacex_last_launch 5eb87d47ffd86e000604b38a
Downloaded spacex_1.jpg
Downloaded spacex_2.jpg
Downloaded spacex_3.jpg
```
#### The code accepts the desired date of the images from the user, downloads these EPIC (Earth Polychromatic Imaging Camera) photos from the NASA website using the API. If there are no photos on the specified date, the code downloads the photos on the nearest date. Photos are saved in the created folder in the directory with the project
- Launching the program to download photos:
```
C:\Users\telegram_project> python uploading_nasa_epic_photos.py 2023-04-20
Downloaded epic_photos_epic_1b_20230219010433
Downloaded epic_photos_epic_1b_20230219010456
Downloaded epic_photos_epic_1b_20230219010239
```
## Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org.](https://dvmn.org/)
