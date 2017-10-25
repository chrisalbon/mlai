Title: Using Mean Color As A Feature  
Slug: using_mean_color_as_a_feature  
Summary: How to use the mean color of an image as a feature using OpenCV in Python with the Shi-Tomasi Corner Detector.     
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
# Load image as BGR
image_bgr = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_COLOR)
```

## Calculate Mean Color Of Each Color Channel


```python
# Calculate the mean of each channel
channels = cv2.mean(image_bgr)

# Swap blue and red values (making it RGB, not BGR)
observation = np.array([(channels[2], channels[1], channels[0])])
```

## Show Values


```python
# Show mean channel values
observation
```




    array([[  90.53204346,  133.11735535,  169.03074646]])



## View Mean Image Colors


```python
# Show image
plt.imshow(observation), plt.axis("off")
plt.show()
```


![png](using_mean_color_as_a_feature_files/using_mean_color_as_a_feature_10_0.png)

