import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('img.jfif') 

if image is None:
    print("Error: Unable to load the image.")
else:
   
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Grayscale Image')
    plt.imshow(grayscale_image, cmap='gray')
    plt.axis('off')

    plt.show()
