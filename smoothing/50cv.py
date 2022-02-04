# smoothing - blur

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


kernel = np.ones((5, 5), np.float32)/25
# (source, destination_img_desired_depth, kernel)
dst = cv2.filter2D(img, -1, kernel)   # destination  image
blur = cv2.blur(img, (5, 5))


titles = ['image', '2D_Conv', 'blur']
images = [img, dst, blur]

for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
