from PIL import Image, ImageFilter
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')

image = Image.open(image_path)

image_boxblur = image.filter(ImageFilter.BoxBlur(radius=20))
image_gaussianblur = image.filter(ImageFilter.GaussianBlur(radius=20))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius=20))

image_boxblur.show()
image_gaussianblur.show()
