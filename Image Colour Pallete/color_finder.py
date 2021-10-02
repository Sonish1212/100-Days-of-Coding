from PIL import Image
from numpy import array, prod
from matplotlib.colors import to_hex
from collections import Counter


def get_image(file_path: str):
    return array(Image.open(file_path))


def get_length(image: array):
    return image.shape[0]*image.shape[1]


def find_top_colors(image: array):
    if len(image.shape) <= 2:
        return False
    colors = map(tuple, image.reshape(prod(image.shape[:-1], image.shape[-1])))
    return Counter(colors).most_common(10)


def rgb_to_hex(rgb: tuple):
    rgb = list(map(lambda x: x/255, rgb))
    return to_hex(rgb, keep_alpha=True).upper()


def reshape_colors(colors: list, length: int):
    return {rgb_to_hex(color): round(count*100/length, 2) for color, count in colors}
