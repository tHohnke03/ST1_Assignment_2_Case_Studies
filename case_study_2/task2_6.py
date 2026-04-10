import cv2
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image = cv2.imread(image_path)

pixel = image[50, 50]
print("Pixel at (50, 50):", pixel)

image[50, 50] = [255, 255, 255]
cv2.imwrite('modified.png', image)
print("Saved modified.png")
