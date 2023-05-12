import argparse
import os

import requests


def fetch_spacex_last_launch(url):
    directory = os.path.join(os.getcwd(), r'space_photos')
    if not os.path.exists(directory):
        os.makedirs(directory)
    response = requests.get(url)
    response.raise_for_status()
    links_to_photos = response.json()["links"]["flickr"]["original"]
    if len(links_to_photos) > 0:
        for index_image, image in enumerate(links_to_photos, 1):
            response = requests.get(image)
            response.raise_for_status()
            image_properties = f'{directory}/spacex_{index_image}{os.path.splitext(image)[1]}'
            with open(image_properties, 'wb') as file:
                file.write(response.content)
                print(f'Downloaded spacex_{image_properties}')
    else:
        print("There are no photos for this launch.")


def main():
    parser = argparse.ArgumentParser('Program Description')
    parser.add_argument('link_id', help='launch id')
    args = parser.parse_args()
    if args.link_id:
        url = f'https://api.spacexdata.com/v5/launches/{args.link_id}'
    else:
        url = 'https://api.spacexdata.com/v5/launches/latest'
    try:
        fetch_spacex_last_launch(url)
    except:
        print("Couldn't get a photo")


if __name__ == "__main__":
    main()
