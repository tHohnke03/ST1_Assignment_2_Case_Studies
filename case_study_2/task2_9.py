import cv2
import os

image1_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image2_path = os.path.join('Assets', 'Insects', 'insect2.jpg')

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)
image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

added = cv2.add(image1, image2_resized)
subtracted = cv2.subtract(image1, image2_resized)

cv2.imshow('Added', added)
cv2.imshow('Subtracted', subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows()
