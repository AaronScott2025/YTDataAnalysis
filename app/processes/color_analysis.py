import colorgram
import requests
from io import BytesIO
from PIL import Image


def get_image_from_url(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    return image


def getColors(image_url):
    image = get_image_from_url(image_url)

    num_colors = 40
    colors = colorgram.extract(image, num_colors)
    color_list = []

    for color in colors:
        color_info = color.rgb
        color_list.append(color_info)

    return color_list