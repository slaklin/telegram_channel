import argparse
import datetime
import os

import requests
from dotenv import load_dotenv


def download_photos_date(date_of_photos, nasa_api):
    directory = os.path.join(os.getcwd(), r'space_photos')
    if not os.path.exists(directory):
        os.makedirs(directory)
    date_picture = datetime.datetime.strptime(date_of_photos, "%Y-%m-%d")
    changed_date = date_picture.strftime("%Y/%m/%d")
    base_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    url_date = f"{base_url}{date_picture}"
    request_parameters = {
        "api_key": nasa_api,
    }
    response = requests.get(url_date, params=request_parameters)
    if response.status_code == 200:
        data = response.json()
        for photo_data in data:
            image_url = f"https://api.nasa.gov/EPIC/archive/natural/{changed_date}/png/{photo_data['image']}" \
                        f".png"
            response = requests.get(image_url, params=request_parameters)
            with open(f'{directory}/photos_{photo_data["image"]}.png', 'wb') as file:
                file.write(response.content)
                print(f'Downloaded epic_photos_{changed_date}')
        return True


def uploading_epic_photos(nasa_api):
    directory = os.path.join(os.getcwd(), r'space_photos')
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    request_parameters = {
        "api_key": nasa_api,
    }
    response = requests.get(url, params=request_parameters)
    data = response.json()
    link = []
    for item in data:
        date = datetime.datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S")
        formatted_date = date.strftime("%Y/%m/%d")
        links = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{item["image"]}' \
                f'.png'
        link.append(links)
    for index_image, image in enumerate(link, 1):
        response = requests.get(image, params=request_parameters)
        response.raise_for_status()
        with open(f'{directory}/epic_photos_{index_image}.png', 'wb') as file:
            file.write(response.content)
            print(f'Downloaded epic_photos_{index_image}')


def main():
    load_dotenv()
    nasa_api = os.getenv("NASA_API_KEY")
    parser = argparse.ArgumentParser('Downloads all NASA photos for a specific date')
    parser.add_argument('date_of_photos', type=str, help='Date in the format "YYYY-MM-DD"')
    args = parser.parse_args()
    date_of_photos = args.date_of_photos
    if download_photos_date(date_of_photos, nasa_api):
        exit()
    else:
        uploading_epic_photos(nasa_api)


if __name__ == "__main__":
    main()