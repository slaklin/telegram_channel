# Downloads a SpaceX launch photo
The code takes the launch ID from the user and downloads all the photos of that moment. If no photos were taken at the time of this launch, downloads the most recent launch in which there are photos.
Photos are saved in the created folder in the directory with the project.

#### Requirements

Python3 should be already installed. Then use pip to install dependencies:
Specify your folder name where the downloaded photos will be saved
```
pip install -r requirements.txt
```
## Example of running a script
- Launching the program to download photos:
```
C:\Users\telegram_project> python fetch_spacex_last_launch 5eb87d47ffd86e000604b38a
Downloaded spacex_1.jpg
Downloaded spacex_2.jpg
Downloaded spacex_3.jpg
```
## Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org.](https://dvmn.org/)