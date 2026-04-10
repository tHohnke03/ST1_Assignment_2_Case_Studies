from PIL import Image, ImageOps
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')

image = Image.open(image_path)

image_mirror = ImageOps.mirror(image)

image_inverted = ImageOps.invert(image_mirror)

image_border = ImageOps.expand(
    image=image_inverted,
    border=50,
    fill=(255, 255, 255)
)

image_border.show()
