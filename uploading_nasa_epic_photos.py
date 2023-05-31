import argparse
import datetime
import os

import requests
from dotenv import load_dotenv


class EmptyDictionary(Exception):
    pass


def sort_photos_by_date(date_of_photos, request_parameters):
    date_picture = datetime.datetime.strptime(date_of_photos, "%Y-%m-%d")
    changed_date = date_picture.strftime("%Y/%m/%d")
    base_url = 'https://api.nasa.gov/EPIC/api/natural/date/'
    url_date = f"{base_url}{date_picture}"
    response = requests.get(url_date, params=request_parameters)
    response.raise_for_status()
    snapshot_data = response.json()
    links_by_date = []
    for photo_title in snapshot_data:
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{changed_date}/png/{photo_title['image']}" \
                    f".png"
        links_by_date.append(image_url)
    if not links_by_date:
        raise EmptyDictionary
    else:
        return links_by_date


def sort_recent_photos(request_parameters):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=request_parameters)
    response.raise_for_status()
    snapshot_data = response.json()
    links_by_date = []
    for parameters_of_link in snapshot_data:
        date = datetime.datetime.strptime(parameters_of_link['date'], "%Y-%m-%d %H:%M:%S")
        formatted_date = date.strftime("%Y/%m/%d")
        link = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{parameters_of_link["image"]}' \
               f'.png'
        links_by_date.append(link)
    return links_by_date


def find_image_links(links_by_date, directory, request_parameters):
    for image_index, image in enumerate(links_by_date, 1):
        upload_photos(image_index, image, directory, request_parameters)


def upload_photos(image_index, image, directory, request_parameters):
    response = requests.get(image, params=request_parameters)
    response.raise_for_status()
    with open(f'{directory}/epic_photos_{image_index}.png', 'wb') as file:
        file.write(response.content)
        print(f'Downloaded epic_photos_{image_index}')


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
    try:
        links_by_date = sort_photos_by_date(date_of_photos, request_parameters)
        find_image_links(links_by_date, directory, request_parameters)
    except EmptyDictionary:
        print('No pictures were taken on the specified date, we upload the pictures according '
              'to the last available date')
        links_by_date = sort_recent_photos(request_parameters)
        find_image_links(links_by_date, directory, request_parameters)


if __name__ == "__main__":
    main()
