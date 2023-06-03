import argparse
import os

import requests
from dotenv import load_dotenv

from fetch_spacex_last_launch import uploading_photos


def find_apod_images(number, nasa_api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    request_parameters = {
        "api_key": nasa_api_key,
        "count": f'{number}',
    }
    response = requests.get(url, params=request_parameters)
    response.raise_for_status()
    links_to_photos = [item['url'] for item in response.json()]
    return links_to_photos


def download_apod_images(links_to_photos, directory):
    uploading_photos(links_to_photos, directory)


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    parser = argparse.ArgumentParser('Download APOD images from NASA')
    parser.add_argument('number_of_photos', type=int, default=10, help='Enter a number of photos')
    args = parser.parse_args()
    number = args.number_of_photos
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    links_to_photos = find_apod_images(number, nasa_api_key)
    download_apod_images(links_to_photos, directory)


if __name__ == "__main__":
    main()
