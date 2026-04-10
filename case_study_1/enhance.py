from PIL import Image, ImageEnhance
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')

image = Image.open(image_path)

vibrance_enhancer = ImageEnhance.Color(image)
contrast_enhancer = ImageEnhance.Contrast(image)
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)

enhanced_image = sharpness_enhancer.enhance(1.5)

image.show()
enhanced_image.show()
