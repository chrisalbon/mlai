Title: Preprocessing Data For Neural Networks    
Slug: preprocessing_data_for_neural_networks    
Summary: How to preprocessing numerical data for neural networks and deep learning in Python.    
Date: 2017-09-25 12:00  
Category: Deep Learning - Keras  
Tags: Basics   
Authors: Chris Albon

Typically, a neural network's parameters are initialized (i.e. created) as small random numbers. Neural networks often behave poorly when the feature values much larger than parameter values. Furthermore, since an observation's feature values will are combined as they pass through individual units, it is important that all features have the same scale.

For these reasons, it is best practice (although not always necessary, for example when we have all binary features) to standardize each feature such that the feature's values have the mean of 0 and the standard deviation of 1. This can be easily accomplished using scikit-learn's `StandardScaler`.

## Preliminaries


```python
# Load libraries
from sklearn import preprocessing
import numpy as np
```

## Create Feature Data


```python
# Create feature
features = np.array([[-100.1, 3240.1], 
                     [-200.2, -234.1], 
                     [5000.5, 150.1], 
                     [6000.6, -125.1], 
                     [9000.9, -673.1]])
```

## Standardize Feature Data


```python
# Create scaler
scaler = preprocessing.StandardScaler()

# Transform the feature
features_standardized = scaler.fit_transform(features)
```

## Show Standardized Features


```python
# Show feature
features_standardized
```




    array([[-1.12541308,  1.96429418],
           [-1.15329466, -0.50068741],
           [ 0.29529406, -0.22809346],
           [ 0.57385917, -0.42335076],
           [ 1.40955451, -0.81216255]])



## Show Standardized Features Summary Statistics


```python
# Print mean and standard deviation
print('Mean:', round(features_standardized[:,0].mean()))
print('Standard deviation:', features_standardized[:,0].std())
```

    Mean: 0.0
    Standard deviation: 1.0

