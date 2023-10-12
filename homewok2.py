import numpy as np
import cv2
img = cv2.imread("pardazesh tasvir\messi and ronaldo.jpg",0)
mean = 0
var = 10
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (667, 1200)) #  np.zeros((224, 224), np.float32)

noisy_image = np.zeros(img.shape, np.float32)

if len(img.shape) == 2:
    noisy_image = img + gaussian
else:
    noisy_image[:, :, 0] = img[:, :, 0] + gaussian
    noisy_image[:, :, 1] = img[:, :, 1] + gaussian
    noisy_image[:, :, 2] = img[:, :, 2] + gaussian

cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
noisy_image = noisy_image.astype(np.uint8)

cv2.imshow("img", img)
cv2.imshow("gaussian", gaussian)
cv2.imshow("noisy", noisy_image)

cv2.waitKey(0)
