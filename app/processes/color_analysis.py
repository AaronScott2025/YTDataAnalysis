from collections import Counter
from typing import List

import requests
from io import BytesIO
from PIL import Image
import colorgram

def get_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def getColors(image_url):
    x = List
    # Get the image from the URL
    image = get_image_from_url(image_url)

    # Save the image to a temporary file
    temp_image_path = 'temp_image.jpg'
    image.save(temp_image_path)

    # Extract colors from the image
    num_colors = 20  # Number of colors you want to extract
    colors = colorgram.extract(temp_image_path, num_colors)

    # Print the colors
    for color in colors:
        rgb = color.rgb  # RGB tuple
        proportion = color.proportion  # Proportion of the image
        x.append(rgb.r+","+rgb.g+","+rgb.b+","+ "|" +proportion)
        print(f'RGB: {rgb}, Percentage of Image: {proportion}')
    return x
if __name__ == '__main__':
    getColors("s")