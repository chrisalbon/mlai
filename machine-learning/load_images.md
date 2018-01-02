Title: Load Images  
Slug: load_images  
Summary: How to load images using OpenCV in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Images    
Authors: Chris Albon

## Preliminaries


```python
# Load library
import cv2
import numpy as np
from matplotlib import pyplot as plt
```

## Load Image As Greyscale


```python
# Load image as grayscale
image = cv2.imread('images/plane.jpg', cv2.IMREAD_GRAYSCALE)

# Show image
plt.imshow(image, cmap='gray'), plt.axis("off")
plt.show()
```


![png](load_images_files/load_images_4_0.png)


## Load Image As RGB


```python
# Load image in color
image_bgr = cv2.imread('images/plane.jpg', cv2.IMREAD_COLOR)

# Convert to RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(image_rgb), plt.axis("off")
plt.show()
```


![png](load_images_files/load_images_6_0.png)


## View Image Data


```python
# Show image data
image
```




    array([[140, 136, 146, ..., 132, 139, 134],
           [144, 136, 149, ..., 142, 124, 126],
           [152, 139, 144, ..., 121, 127, 134],
           ..., 
           [156, 146, 144, ..., 157, 154, 151],
           [146, 150, 147, ..., 156, 158, 157],
           [143, 138, 147, ..., 156, 157, 157]], dtype=uint8)




```python
# Show dimensions
image.shape
```




    (2270, 3600)


