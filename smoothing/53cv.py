# smoothing - median filter (replaces pixels with median of it neighbouring pixels) best for salt&pepper noise
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('water.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)   # destination  image
blur = cv2.blur(img, (5, 5))
gaus = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img,  5)  # 2nd variabe is kernel size(5,5)

titles = ['image', '2D_Conv', 'blur', 'GaussianBlur', 'median']
images = [img, dst, blur, gaus, median]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
