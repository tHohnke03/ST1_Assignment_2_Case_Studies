import cv2
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png', gray)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
