import cv2
import os

image_path = os.path.join('Assets', 'Insects', 'insect1.jpg')
image = cv2.imread(image_path)

print("Image shape:", image.shape)
print("Image dtype:", image.dtype)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
