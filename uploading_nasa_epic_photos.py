import argparse
import datetime
import os

import requests
from dotenv import load_dotenv


class EmptyDictionary(Exception):
    pass


def sort_photos_by_date(date_of_photos, nasa_access_token):
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    date_picture = datetime.datetime.strptime(date_of_photos, "%Y-%m-%d")
    changed_date = date_picture.strftime("%Y/%m/%d")
    base_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    url_date = f"{base_url}{date_picture}"
    request_parameters = {
        "api_key": nasa_access_token,
    }
    response = requests.get(url_date, params=request_parameters)
    response.raise_for_status()
    dictionary = response.json()
    download_links = []
    for photo_title in dictionary:
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{changed_date}/png/{photo_title['image']}" \
                        f".png"
        download_links.append(image_url)
    if not download_links:
        raise EmptyDictionary
    else:
        upload_photos(download_links, directory, request_parameters)


def sort_recent_photos(nasa_access_token):
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    request_parameters = {
        "api_key": nasa_access_token,
    }
    response = requests.get(url, params=request_parameters)
    response.raise_for_status()
    dictionary = response.json()
    download_links = []
    for parameters_of_link in dictionary:
        date = datetime.datetime.strptime(parameters_of_link['date'], "%Y-%m-%d %H:%M:%S")
        formatted_date = date.strftime("%Y/%m/%d")
        link = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{parameters_of_link["image"]}' \
               f'.png'
        download_links.append(link)
    upload_photos(download_links, directory, request_parameters)


def upload_photos(download_links, directory, request_parameters):
    for image_index, image in enumerate(download_links, 1):
        response = requests.get(image, params=request_parameters)
        response.raise_for_status()
        with open(f'{directory}/epic_photos_{image_index}.png', 'wb') as file:
            file.write(response.content)
            print(f'Downloaded epic_photos_{image_index}')


def main():
    load_dotenv()
    nasa_access_token = os.getenv("NASA_API_KEY")
    parser = argparse.ArgumentParser('Downloads all NASA photos for a specific date')
    parser.add_argument('date_of_photos', type=str, help='Date in the format "YYYY-MM-DD"')
    args = parser.parse_args()
    date_of_photos = args.date_of_photos
    try:
        sort_photos_by_date(date_of_photos, nasa_access_token)
    except EmptyDictionary:
        sort_recent_photos(nasa_access_token)


if __name__ == "__main__":
    main()
