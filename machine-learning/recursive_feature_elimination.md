Title: Recursive Feature Elimination  
Slug: recursive_feature_elimination  
Summary: How to do recursive feature elimination for machine learning in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Feature Selection
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from sklearn.datasets import make_regression
from sklearn.feature_selection import RFECV
from sklearn import datasets, linear_model
import warnings

# Suppress an annoying but harmless warning
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")
```

## Create Data


```python
# Generate features matrix, target vector, and the true coefficients
X, y = make_regression(n_samples = 10000,
                       n_features = 100,
                       n_informative = 2,
                       random_state = 1)
```

## Create Linear Model


```python
# Create a linear regression
ols = linear_model.LinearRegression()
```

## Conduct Recursive Feature Elimination


```python
# Create recursive feature eliminator that scores features by mean squared errors
rfecv = RFECV(estimator=ols, step=1, scoring='neg_mean_squared_error')

# Fit recursive feature eliminator 
rfecv.fit(X, y)

# Recursive feature elimination
rfecv.transform(X)
```




    array([[ 0.00850799,  0.7031277 , -1.2416911 , -0.25651883, -0.10738769],
           [-1.07500204,  2.56148527,  0.5540926 , -0.72602474, -0.91773159],
           [ 1.37940721, -1.77039484, -0.59609275,  0.51485979, -1.17442094],
           ..., 
           [-0.80331656, -1.60648007,  0.37195763,  0.78006511, -0.20756972],
           [ 0.39508844, -1.34564911, -0.9639982 ,  1.7983361 , -0.61308782],
           [-0.55383035,  0.82880112,  0.24597833, -1.71411248,  0.3816852 ]])



## Number Of Features Remaining


```python
# Number of best features
rfecv.n_features_
```




    5


