import cv2
import os

image1_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image2_path = os.path.join('Assets', 'Insects', 'insect2.jpg')

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

blended = cv2.addWeighted(image1, 0.6, image2_resized, 0.4, 0)

cv2.imshow('Blended', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
