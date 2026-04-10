import cv2
import numpy as np
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image = cv2.imread(image_path)

inverted = 255 - image

combined = np.hstack((image, inverted))
cv2.imshow('Original | Inverted', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
