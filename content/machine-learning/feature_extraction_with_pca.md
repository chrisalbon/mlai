Title: Feature Extraction With PCA   
Slug: feature_extraction_with_pca   
Summary: Feature extraction with PCA using scikit-learn.   
Date: 2017-09-13 12:00   
Category: Machine Learning   
Tags: Feature Engineering  
Authors: Chris Albon   

[Principle Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) (PCA) is a common feature extraction method in data science. Technically, PCA finds the eigenvectors of a covariance matrix with the highest eigenvalues and then uses those to project the data into a new subspace of equal or less dimensions. Practically, PCA converts a matrix of `n` features into a new dataset of (hopefully) less than `n` features. That is, it reduces the number of features by constructing a new, smaller number variables which capture a signficant portion of the information found in the original features. However, the goal of this tutorial is not to explain the concept of PCA, that is done very well elsewhere, but rather to demonstrate PCA in action.

## Preliminaries


```python
# Import packages
import numpy as np
from sklearn import decomposition, datasets
from sklearn.preprocessing import StandardScaler
```

## Load Features


```python
# Load the breast cancer dataset
dataset = datasets.load_breast_cancer()

# Load the features
X = dataset.data
```

Notice that original data contains 569 observations and 30 features.


```python
# View the shape of the dataset
X.shape
```




    (569, 30)



Here is what the data looks like.


```python
# View the data
X
```




    array([[  1.79900000e+01,   1.03800000e+01,   1.22800000e+02, ...,
              2.65400000e-01,   4.60100000e-01,   1.18900000e-01],
           [  2.05700000e+01,   1.77700000e+01,   1.32900000e+02, ...,
              1.86000000e-01,   2.75000000e-01,   8.90200000e-02],
           [  1.96900000e+01,   2.12500000e+01,   1.30000000e+02, ...,
              2.43000000e-01,   3.61300000e-01,   8.75800000e-02],
           ..., 
           [  1.66000000e+01,   2.80800000e+01,   1.08300000e+02, ...,
              1.41800000e-01,   2.21800000e-01,   7.82000000e-02],
           [  2.06000000e+01,   2.93300000e+01,   1.40100000e+02, ...,
              2.65000000e-01,   4.08700000e-01,   1.24000000e-01],
           [  7.76000000e+00,   2.45400000e+01,   4.79200000e+01, ...,
              0.00000000e+00,   2.87100000e-01,   7.03900000e-02]])



## Standardize Features


```python
# Create a scaler object
sc = StandardScaler()

# Fit the scaler to the features and transform
X_std = sc.fit_transform(X)
```

## Conduct PCA

Notice that PCA contains a parameter, the number of components. This is the number of output features and will need to be tuned.


```python
# Create a pca object with the 2 components as a parameter
pca = decomposition.PCA(n_components=2)

# Fit the PCA and transform the data
X_std_pca = pca.fit_transform(X_std)
```

## View New Features 

After the PCA, the new data has been reduced to two features, with the same number of rows as the original feature.


```python
# View the new feature data's shape
X_std_pca.shape
```




    (569, 2)




```python
# View the new feature data
X_std_pca
```




    array([[  9.19283683,   1.94858307],
           [  2.3878018 ,  -3.76817174],
           [  5.73389628,  -1.0751738 ],
           ..., 
           [  1.25617928,  -1.90229671],
           [ 10.37479406,   1.67201011],
           [ -5.4752433 ,  -0.67063679]])


