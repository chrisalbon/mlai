Title: Loading scikit-learn's Digits Dataset  
Slug: loading_scikit-learns_digits-dataset  
Summary: Loading the built-in digits datasets of scikit-learn.   
Date: 2016-08-31 12:00  
Category: Machine Learning  
Tags: Basics  
Authors: Chris Albon 

## Preliminaries


```python
# Load libraries
from sklearn import datasets
import matplotlib.pyplot as plt 
```

## Load Digits Dataset

Digits is a dataset of handwritten digits. Each feature is the intensity of one pixel of an 8 x 8 image.


```python
# Load digits dataset
digits = datasets.load_digits()

# Create feature matrix
X = digits.data

# Create target vector
y = digits.target

# View the first observation's feature values
X[0]
```




    array([  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.,   0.,   0.,  13.,
            15.,  10.,  15.,   5.,   0.,   0.,   3.,  15.,   2.,   0.,  11.,
             8.,   0.,   0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.,   0.,
             5.,   8.,   0.,   0.,   9.,   8.,   0.,   0.,   4.,  11.,   0.,
             1.,  12.,   7.,   0.,   0.,   2.,  14.,   5.,  10.,  12.,   0.,
             0.,   0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.])



The observation's feature values are presented as a vector. However, by using the `images` method we can load the the same feature values as a matrix and then visualize the actual handwritten character:


```python
# View the first observation's feature values as a matrix
digits.images[0]
```




    array([[  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.],
           [  0.,   0.,  13.,  15.,  10.,  15.,   5.,   0.],
           [  0.,   3.,  15.,   2.,   0.,  11.,   8.,   0.],
           [  0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.],
           [  0.,   5.,   8.,   0.,   0.,   9.,   8.,   0.],
           [  0.,   4.,  11.,   0.,   1.,  12.,   7.,   0.],
           [  0.,   2.,  14.,   5.,  10.,  12.,   0.,   0.],
           [  0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.]])




```python
# Visualize the first observation's feature values as an image
plt.gray() 
plt.matshow(digits.images[0]) 
plt.show()
```


    <matplotlib.figure.Figure at 0x1068494a8>



![png](loading_scikit-learns_digits-dataset_files/loading_scikit-learns_digits-dataset_7_1.png)

