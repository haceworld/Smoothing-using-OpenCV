# canny edges ===> detection of edges
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(img, 100, 200)  #(img, 1st_threshold_value, 2nd_threshold_value)


titles = ['image']
images = [canny]

for i in range(1):
    plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()




