from PIL import Image
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')

image = Image.open(image_path)

print(image.size)
print(image.filename)
print(image.format)

image = image.transpose(Image.Transpose.ROTATE_90)
image.show()

img_rotated = image.rotate(30)
img_rotated.save('img_rotated.png', 'PNG')
print("Saved img_rotated.png")
