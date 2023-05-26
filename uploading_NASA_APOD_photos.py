import argparse
import os

import requests
from dotenv import load_dotenv


def find_apod_images(url, number, nasa_api_key):
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    request_parameters = {
        "api_key": nasa_api_key,
        "count": f'{number}',
    }
    response = requests.get(url, params=request_parameters)
    response.raise_for_status()
    links = [item['url'] for item in response.json()]
    return links, directory


def find_apod_links(links, directory):
    for image_index, image in enumerate(links, 1):
        download_apod_images(image_index, image, directory)


def download_apod_images(image_index, image, directory):
    response = requests.get(image)
    response.raise_for_status()
    download_link = f'{directory}/apod_photos_{image_index}{os.path.splitext(image)[1]}'
    with open(download_link, 'wb') as file:
        file.write(response.content)
        print(f'Downloaded apod_photos_{download_link}')


def main():
    url = 'https://api.nasa.gov/planetary/apod'
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    parser = argparse.ArgumentParser('Download APOD images from NASA')
    parser.add_argument('number_of_photos', type=int, default=10, help='Enter a number of photos')
    args = parser.parse_args()
    number = args.number_of_photos
    links, directory = find_apod_images(url, number, nasa_api_key)
    find_apod_links(links, directory)


if __name__ == "__main__":
    main()
