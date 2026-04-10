from PIL import Image
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')

image = Image.open(image_path)

print(image.getpixel((0, 0)))

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x, y))[0] == 0:
            image.putpixel((x, y), (200, 20, 20))

image.show()
