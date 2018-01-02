Title: Random Forest Regression  
Slug: random_forest_regression  
Summary: Training a random forest regressor in scikit-learn.  
Date: 2017-09-21 12:00  
Category: Machine Learning  
Tags: Trees And Forests  
Authors: Chris Albon  

## Preliminaries


```python
# Load libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets
```

## Load Boston Housing Data


```python
# Load data with only two features
boston = datasets.load_boston()
X = boston.data[:,0:2]
y = boston.target
```

## Create Random Forest Regressor


```python
# Create decision tree classifer object
regr = RandomForestRegressor(random_state=0, n_jobs=-1)
```

## Train Random Forest Regressor


```python
# Train model
model = regr.fit(X, y)
```
