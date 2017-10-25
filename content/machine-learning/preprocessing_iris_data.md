Title: Preprocessing Iris Data  
Slug: preprocessing_iris_data  
Summary: Preprocessing iris data using scikit learn.  
Date: 2016-09-21 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

## Preliminaries


```python
from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
```

## Load Data


```python
# Load the iris data
iris = datasets.load_iris()

# Create a variable for the feature data
X = iris.data

# Create a variable for the target data
y = iris.target
```

## Split Data For Cross Validation


```python
# Random split the data into four new datasets, training features, training outcome, test features, 
# and test outcome. Set the size of the test data to be 30% of the full dataset.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

## Standardize Feature Data


```python
# Load the standard scaler
sc = StandardScaler()

# Compute the mean and standard deviation based on the training data
sc.fit(X_train)

# Scale the training data to be of mean 0 and of unit variance
X_train_std = sc.transform(X_train)

# Scale the test data to be of mean 0 and of unit variance
X_test_std = sc.transform(X_test)
```


```python
# Feature Test Data, non-standardized
X_test[0:5]
```




    array([[ 6.1,  2.8,  4.7,  1.2],
           [ 5.7,  3.8,  1.7,  0.3],
           [ 7.7,  2.6,  6.9,  2.3],
           [ 6. ,  2.9,  4.5,  1.5],
           [ 6.8,  2.8,  4.8,  1.4]])




```python
# Feature Test Data, standardized.
X_test_std[0:5]
```




    array([[ 0.3100623 , -0.49582097,  0.48403749, -0.05143998],
           [-0.17225683,  1.92563026, -1.26851205, -1.26670948],
           [ 2.23933883, -0.98011121,  1.76924049,  1.43388941],
           [ 0.18948252, -0.25367584,  0.36720086,  0.35364985],
           [ 1.15412078, -0.49582097,  0.54245581,  0.21861991]])


