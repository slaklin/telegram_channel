# Downloads all EPIC NASA photos
The code accepts the desired date of the images from the user, downloads these EPIC (Earth Polychromatic Imaging Camera) photos from the NASA website using the API. If there are no photos on the specified date, the code downloads the photos on the nearest date. Photos are saved in the created folder in the directory with the project
 

## How to install
Create [api.nasa.gov](https://api.nasa.gov/#epic) Generate API Key for work with API.

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
C:\Users\telegram_project> python uploading_nasa_epic_photos.py 2023-04-20
Downloaded epic_photos_epic_1b_20230219010433
Downloaded epic_photos_epic_1b_20230219010456
Downloaded epic_photos_epic_1b_20230219010239
```

## Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org.](https://dvmn.org/)
