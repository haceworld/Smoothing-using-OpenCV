# image gradient - the directional change in the intensity or color in an image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)  # cv2.CV_64F ===> a data type, ksize = kernel_size
lap = np.uint8(np.absolute(lap))
# (img, data_type, dx(0 or 1), dy(0 or 1), kernel_size)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
 

titles = ['image', 'Laplacian', 'sobelX', 'sobelY']
images = [img, lap, sobelX, sobelY]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
