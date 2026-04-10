import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
img = mpimg.imread(image_path)

gray = np.mean(img, axis=2).astype(np.uint8)

plt.imsave('gray_insect.png', gray, cmap='gray')

reloaded = mpimg.imread('gray_insect.png')
plt.imshow(reloaded, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()
