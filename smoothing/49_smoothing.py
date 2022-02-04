# smoothing - using filters to remove noise in images (filters: homogeneous, gaussian, median, bilateral)
# homogeneous filter: each output pixel is mean of its kernek neighbors

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


kernel = np.ones((5, 5), np.float32)/25
# (source, destination_img_desired_depth, kernel)
dst = cv2.filter2D(img, -1, kernel)   # destination  image



titles = ['image', '2D_Conv']
images = [img, dst]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
