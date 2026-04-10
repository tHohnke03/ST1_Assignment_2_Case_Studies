import matplotlib.image as mpimg
import numpy as np
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
img = mpimg.imread(image_path)

img_array = np.array(img)

print("Array shape:", img_array.shape)
print("Data type:", img_array.dtype)
print("Min pixel value:", img_array.min())
print("Max pixel value:", img_array.max())
