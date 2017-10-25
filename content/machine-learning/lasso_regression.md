Title: Lasso Regression    
Slug: lasso_regression    
Summary: How to conduct lasso regression in scikit-learn for machine learning in Python.    
Date: 2017-09-18 12:00  
Category: Machine Learning  
Tags: Linear Regression   
Authors: Chris Albon

## Preliminaries


```python
# Load library
from sklearn.linear_model import Lasso
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
```

## Load Boston Housing Dataset


```python
# Load data
boston = load_boston()
X = boston.data
y = boston.target
```

## Standardize Features


```python
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
```

## Fit Ridge Regression

The hyperparameter, $\alpha$, lets us control how much we penalize the coefficients, with higher values of $\alpha$ creating simpler modelers. The ideal value of $\alpha$ should be tuned like any other hyperparameter. In scikit-learn, $\alpha$ is set using the `alpha` parameter.


```python
# Create lasso regression with alpha value
regr = Lasso(alpha=0.5)

# Fit the linear regression
model = regr.fit(X_std, y)
```
