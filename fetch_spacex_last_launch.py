import argparse
import os

import requests


def fetch_spacex_last_launch(url):
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    links_to_photos = response.json()["links"]["flickr"]["original"]
    return links_to_photos, directory


def find_image_links(links_to_photos, directory):
    for image_index, image in enumerate(links_to_photos, 1):
        download_the_last_launch(image_index, image, directory)


def download_the_last_launch(image_index, image, directory):
    response = requests.get(image)
    response.raise_for_status()
    download_link = f'{directory}/spacex_{image_index}{os.path.splitext(image)[1]}'
    with open(download_link, 'wb') as file:
        file.write(response.content)
        print(f'Downloaded spacex_{download_link}')


def main():
    parser = argparse.ArgumentParser("The program downloads photos from the launch"
                                     "of Spacex rockets by the specified ID")
    parser.add_argument('--link_id', default='latest', help='Enter the startup ID')
    args = parser.parse_args()
    try:
        url = f'https://api.spacexdata.com/v5/launches/{args.link_id}'
        links_to_photos, directory = fetch_spacex_last_launch(url)
        find_image_links(links_to_photos, directory)
    except requests.exceptions.HTTPError:
        print('Incorrect or invalid startup ID is specified')


if __name__ == "__main__":
    main()
