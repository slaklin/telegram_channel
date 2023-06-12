import argparse
import os

import requests


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    links_to_photos = response.json()["links"]["flickr"]["original"]
    return links_to_photos


def uploading_photos(links_to_photos, directory, **request_parameters):
    for image_index, image in enumerate(links_to_photos, 1):
        response = requests.get(image, params=request_parameters)
        response.raise_for_status()
        file_path = f"{directory}/space_photos{image_index}{os.path.splitext(image)[1]}"
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f'Downloaded {file_path}')


def main():
    parser = argparse.ArgumentParser("The program downloads photos from the launch"
                                     "of Spacex rockets by the specified ID")
    parser.add_argument('--link_id', default='latest', help='Enter the startup ID')
    args = parser.parse_args()
    directory = os.path.join(os.getcwd(), r'space_photos')
    os.makedirs(directory, exist_ok=True)
    try:
        url = f'https://api.spacexdata.com/v5/launches/{args.link_id}'
        links_to_photos = fetch_spacex_last_launch(url)
        uploading_photos(links_to_photos, directory)
    except requests.exceptions.HTTPError:
        print('Incorrect or invalid startup ID is specified')


if __name__ == "__main__":
    main()
