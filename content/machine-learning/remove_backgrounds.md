Title: Remove Backgrounds  
Slug: remove_backgrounds  
Summary: How to remove the backgrounds in images using OpenCV in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Images    
Authors: Chris Albon

<a alt="grabcut" href="https://machinelearningflashcards.com">
    <img src="remove_backgrounds/Grabcut_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt
```

## Load Image


```python
# Load image
image_bgr = cv2.imread('images/plane_256x256.jpg')
```

## Convert To RGB


```python
# Convert to RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
```

## Draw Rectangle Around Foreground


```python
# Rectange values: start x, start y, width, height
rectangle = (0, 56, 256, 150)
```

## Apply GrabCut


```python
# Create initial mask
mask = np.zeros(image_rgb.shape[:2], np.uint8)

# Create temporary arrays used by grabCut
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Run grabCut
cv2.grabCut(image_rgb, # Our image
            mask, # The Mask
            rectangle, # Our rectangle
            bgdModel, # Temporary array for background
            fgdModel, # Temporary array for background
            5, # Number of iterations
            cv2.GC_INIT_WITH_RECT) # Initiative using our rectangle

# Create mask where sure and likely backgrounds set to 0, otherwise 1
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

# Multiply image with new mask to subtract background
image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]
```

## Show image


```python
# Show image
plt.imshow(image_rgb_nobg), plt.axis("off")
plt.show()
```


![png](remove_backgrounds_files/remove_backgrounds_13_0.png)

