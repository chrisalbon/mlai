Title: Blurring Images  
Slug: blurring_images  
Summary: How to blurring images using OpenCV in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Images    
Authors: Chris Albon

## Preliminaries


```python
# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt
```

## Load Image As Greyscale


```python
# Load image as grayscale
image = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
```

## Blur Image


```python
# Blur image
image_blurry = cv2.blur(image, (5,5))
```

## View Image


```python
# Show image
plt.imshow(image_blurry, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()
```


![png](blurring_images_files/blurring_images_8_0.png)

