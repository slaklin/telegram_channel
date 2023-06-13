import argparse
import datetime
import os

import requests
from dotenv import load_dotenv

from fetch_spacex_last_launch import downloads_photos_to_folder


def generates_links_by_date(date_of_photos, request_parameters):
    date_picture = datetime.datetime.strptime(date_of_photos, "%Y-%m-%d")
    changed_date = date_picture.strftime("%Y/%m/%d")
    base_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    url_date = f'{base_url}{date_picture}'
    response = requests.get(url_date, params=request_parameters)
    response.raise_for_status()
    information_on_request = response.json()
    links_to_photos = []
    for photo_title in information_on_request:
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{changed_date}/png/{photo_title['image']}" \
                    f".png"
        links_to_photos.append(image_url)
    return links_to_photos


def generates_links_last_date(request_parameters):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=request_parameters)
    response.raise_for_status()
    information_on_request = response.json()
    links_to_photos = []
    for parameters_of_link in information_on_request:
        date = datetime.datetime.strptime(parameters_of_link['date'], "%Y-%m-%d %H:%M:%S")
        formatted_date = date.strftime("%Y/%m/%d")
        link = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{parameters_of_link['image']}" \
               f".png"
        links_to_photos.append(link)
    return links_to_photos


def main():
    load_dotenv()
    nasa_access_token = os.getenv("NASA_API_KEY")
    parser = argparse.ArgumentParser('Downloads all NASA photos for a specific date')
    parser.add_argument('date_of_photos', type=str, help='Date in the format "YYYY-MM-DD"')
    args = parser.parse_args()
    date_of_photos = args.date_of_photos
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    request_parameters = {
        "api_key": nasa_access_token,
    }
    links_to_photos = generates_links_by_date(date_of_photos, request_parameters)
    downloads_photos_to_folder(links_to_photos, directory, **request_parameters)
    if not links_to_photos:
        print('No pictures were taken on the specified date, we upload the pictures according '
              'to the last available date')
        links_to_photos = generates_links_last_date(request_parameters)
        downloads_photos_to_folder(links_to_photos, directory, **request_parameters)


if __name__ == "__main__":
    main()
