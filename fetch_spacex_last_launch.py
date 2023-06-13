import argparse
import os

import requests

from downloads_photos_to_folder import downloads_photos_to_folder


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    links_to_photos = response.json()['links']['flickr']['original']
    return links_to_photos


def main():
    parser = argparse.ArgumentParser('The program downloads photos from the launch'
                                     'of Spacex rockets by the specified ID')
    parser.add_argument('--link_id', default='latest', help='Enter the startup ID')
    args = parser.parse_args()
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    try:
        url = f'https://api.spacexdata.com/v5/launches/{args.link_id}'
        links_to_photos = fetch_spacex_last_launch(url)
        downloads_photos_to_folder(links_to_photos, directory)
    except requests.exceptions.HTTPError:
        print('Incorrect or invalid startup ID is specified')


if __name__ == "__main__":
    main()
