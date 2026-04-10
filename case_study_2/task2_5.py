import cv2
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image = cv2.imread(image_path)

copy = image.copy()
cv2.circle(copy, (100, 100), 50, (0, 0, 255), 2)

cv2.imshow('Red Circle', copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
