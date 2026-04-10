import cv2
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image = cv2.imread(image_path)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

cv2.imshow('Hue', h)
cv2.imshow('Saturation', s)
cv2.imshow('Value', v)
cv2.waitKey(0)
cv2.destroyAllWindows()
