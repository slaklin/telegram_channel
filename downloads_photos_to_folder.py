import requests
import os


def downloads_photos_to_folder(links_to_photos, directory, **request_parameters):
    for image_index, image in enumerate(links_to_photos, 1):
        response = requests.get(image, params=request_parameters)
        response.raise_for_status()
        file_path = f'{directory}/space_photos{image_index}{os.path.splitext(image)[1]}'
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded {file_path}')