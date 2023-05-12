import argparse
import os
import urllib
from urllib.parse import urlsplit

import requests
from dotenv import load_dotenv


def download_apod_images(url, number):
    directory = os.path.join(os.getcwd(), r'space_photos')
    if not os.path.exists(directory):
        os.makedirs(directory)
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    request_parameters = {
        "api_key": nasa_api_key,
        "count": f'{number}',
    }
    converted_parameters = urllib.parse.urlencode(request_parameters)
    response = requests.get(url, params=converted_parameters)
    links = []
    for item in response.json():
        links.append(item['url'])
    for index_image, image in enumerate(links, 1):
        response = requests.get(image)
        response.raise_for_status()
        image_properties = f'{directory}/apod_photos_{index_image}{os.path.splitext(image)[1]}'
        with open(image_properties, 'wb') as file:
            file.write(response.content)
            print(f'Downloaded apod_photos_{image_properties}')


def main():
    url = 'https://api.nasa.gov/planetary/apod'
    parser = argparse.ArgumentParser('Download APOD images from NASA')
    parser.add_argument('number_of_photos', type=int, default=10, help='Enter a number of photos')
    args = parser.parse_args()
    number = args.number_of_photos
    download_apod_images(url, number)


if __name__ == "__main__":
    main()
