import cv2
import numpy as np
import matplotlib.pyplot as plt

img = input("image address: ")
image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

edges = cv2.Canny(image, 100, 200)

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Detected Edges')
plt.axis('off')

plt.show()