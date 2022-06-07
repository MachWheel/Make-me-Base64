import base64
import os

from . import txt


def read_images(folder) -> list[str]:
    extensions = '.png', '.ico', '.gif'
    files = os.listdir(folder)
    images = [f for f in files if f.endswith(extensions)]
    return images


def get_base64(img_file: str, folder=''):
    filepath = os.path.join(folder, img_file) if folder else img_file
    with open(filepath, 'rb') as file:
        contents = file.read()
    return base64.b64encode(contents)


def clean_file_name(file_name):
    forbidden = '-', '.', ' '
    for char in forbidden:
        file_name = file_name.replace(char, '_')
    return file_name


def write_contents(folder: str, contents: list[str]):
    output_path = os.path.join(folder, txt.OUT_FILE)
    with open(output_path, 'w') as file:
        [file.write(line) for line in contents]
