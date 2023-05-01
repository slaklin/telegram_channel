# Вownload the required number of APOD photos
The program downloads from the NASA website the number of APOD (Astronomy Picture of the Day) photos specified by the user in the original format. Photos are saved in the created folder in the directory with the project.
## How to install
Create [api.nasa.gov](https://api.nasa.gov/#apod) Generate API Key for work with API.
#### Requirements

Python3 should be already installed. Then use pip to install dependencies:
Specify your folder name where the downloaded photos will be saved
```
pip install -r requirements.txt
```
### Create an environment

#### Environment variables
- NASA_API_KEY

1. Place the `.env` file in the root folder of your project.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:
```
$ cat .env
NASA_API_KEY=1a5d754733b01560143c70238efa4esad1taec48
```
## Example of running a script
- Launching the program to download photos:
```
C:\Users\telegram_project> python uploading_NASA_APOD_photos.py 3
Downloaded apod_photos_1.jpg
Downloaded apod_photos_2.jpg
Downloaded apod_photos_3.gif
```
## Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org.](https://dvmn.org/)