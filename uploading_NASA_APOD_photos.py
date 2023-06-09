import argparse
import os

import requests
from dotenv import load_dotenv

from downloads_photos_to_folder import downloads_photos_to_folder


def find_apod_images(number, nasa_api_key, directory):
    url = 'https://api.nasa.gov/planetary/apod'
    request_parameters = {
        "api_key": nasa_api_key,
        "count": f'{number}',
    }
    response = requests.get(url, params=request_parameters)
    response.raise_for_status()
    links_to_photos = [item['url'] for item in response.json()]
    downloads_photos_to_folder(links_to_photos, directory)


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    parser = argparse.ArgumentParser('Download APOD images from NASA')
    parser.add_argument('number_of_photos', type=int, default=10, help='Enter a number of photos')
    args = parser.parse_args()
    number = args.number_of_photos
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    find_apod_images(number, nasa_api_key, directory)


if __name__ == "__main__":
    main()
