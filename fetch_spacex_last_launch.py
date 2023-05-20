import argparse
import os

import requests


def fetch_spacex_last_launch(url):
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    links_to_photos = response.json()["links"]["flickr"]["original"]
    download_the_last_launch(links_to_photos, directory)


def download_the_last_launch(links_to_photos, directory):
    for index_image, image in enumerate(links_to_photos, 1):
        response = requests.get(image)
        response.raise_for_status()
        download_link = f'{directory}/spacex_{index_image}{os.path.splitext(image)[1]}'
        with open(download_link, 'wb') as file:
            file.write(response.content)
            print(f'Downloaded spacex_{download_link}')


def main():
    parser = argparse.ArgumentParser('Program Description')
    parser.add_argument('--link_id', default='latest', help='launch id')
    args = parser.parse_args()
    try:
        url = f'https://api.spacexdata.com/v5/launches/{args.link_id}'
        fetch_spacex_last_launch(url)
    except requests.exceptions.HTTPError:
        print('Incorrect or invalid startup ID is specified')


if __name__ == "__main__":
    main()
