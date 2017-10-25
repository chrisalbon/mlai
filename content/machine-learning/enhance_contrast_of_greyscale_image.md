Title: Enhance Contrast Of Greyscale Image  
Slug: enhance_contrast_of_greyscale_image  
Summary: How to enhance the contrast of images using OpenCV in Python.     
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

## Enhance Image


```python
# Enhance image
image_enhanced = cv2.equalizeHist(image)
```

## View Image


```python
# Show image
plt.imshow(image_enhanced, cmap='gray'), plt.axis("off")
plt.show()
```


![png](enhance_contrast_of_greyscale_image_files/enhance_contrast_of_greyscale_image_8_0.png)

