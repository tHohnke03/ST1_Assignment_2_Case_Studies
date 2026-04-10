from PIL import Image
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')

image = Image.open(image_path)

image_transpose = image.transpose(Image.Transpose.ROTATE_90)

image_rotate = image.rotate(45, expand=False, center=(0, 0))

image_crop = image.crop((100, 100, 400, 400))

image_resize = image.resize((500, 300))

combined_image = image.transpose(Image.Transpose.ROTATE_90).resize((600, 400)).rotate(10)
combined_image.show()
