import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
img = mpimg.imread(image_path)

plt.imshow(img)
plt.title('Insect Image')
plt.axis('off')
plt.show()
