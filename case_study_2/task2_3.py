import cv2
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image = cv2.imread(image_path)

resized = cv2.resize(image, (400, 300))

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
