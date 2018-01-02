Title: Shi-Tomasi Corner Detector  
Slug: ski-tomasi_corner_detector  
Summary: How to detect corners images using OpenCV in Python with the Shi-Tomasi Corner Detector.     
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

## Load image


```python
# Load images
image_bgr = cv2.imread('images/plane_256x256.jpg')
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
```

## Define Corner Parameters


```python
# Number of corners to detect
corners_to_detect = 10
minimum_quality_score = 0.05
minimum_distance = 25
```

## Detect Corners


```python
# Detect corners
corners = cv2.goodFeaturesToTrack(image_gray, 
                                  corners_to_detect, 
                                  minimum_quality_score,
                                  minimum_distance)
corners = np.float32(corners)
```

## Mark Corners


```python
# Draw white circle at each corner
for corner in corners:
    x, y = corner[0]
    cv2.circle(image_bgr, (x,y), 10, (255,255,255), -1)
```

## View Image


```python
# Convert to grayscale
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

# Show image
plt.imshow(image_gray, cmap='gray'), plt.axis("off")
plt.show()
```


![png](ski-tomasi_corner_detector_files/ski-tomasi_corner_detector_12_0.png)

