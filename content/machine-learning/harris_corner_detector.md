Title: Harris Corner Detector  
Slug: harris_corner_detector  
Summary: How to detect corners images using OpenCV in Python with the Harris Corner Detector.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Images    
Authors: Chris Albon

The Harris Corner Detector is a commonly used method of detecting the intersection of two edges. It looks for windows (also called neighborhoods or patches) where small movements of the window (imagine shaking the window) creates big changes in the contents of the pixels inside the window.

## Preliminaries


```python
# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt
```

## Load image


```python
# Load image as grayscale
image_bgr = cv2.imread('images/plane_256x256.jpg')
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
image_gray = np.float32(image_gray)
```

## Define Corner Parameters


```python
# Set corner detector parameters
block_size = 2
aperture = 29
free_parameter = 0.04
```

## Detect Corners


```python
# Detect corners
detector_responses = cv2.cornerHarris(image_gray, block_size, aperture, free_parameter)
```

## Mark Corners


```python
# Large corner markers
detector_responses = cv2.dilate(detector_responses, None)

# Only keep detector responses greater than threshold, mark as white
threshold = 0.02
image_bgr[detector_responses > threshold * detector_responses.max()] = [255,255,255]
```

## View Image


```python
# Convert to grayscale
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

# Show image
plt.imshow(image_gray, cmap='gray'), plt.axis("off")
plt.show()
```


![png](harris_corner_detector_files/harris_corner_detector_13_0.png)

