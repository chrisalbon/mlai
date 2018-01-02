Title: Installing OpenCV  
Slug: installing_opencv  
Summary: How to install OpenCV in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Images    
Authors: Chris Albon

While there are a number of good libraries out there, OpenCV is the most popular and documented library for handling images. One of the biggest hurdles to using OpenCV is installing it. However, fortunately we can use Anaconda's package manager tool conda to install OpenCV in a single line of code in our terminal: 

`conda install --channel https://conda.anaconda.org/menpo opencv3`

Afterwards, we can check the installation by opening a notebook, importing OpenCV, and checking the version number (3.1.0):


```python
# Load library
import cv2

# View version number
cv2.__version__
```




    '3.2.0'


