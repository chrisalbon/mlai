Title: Ridge Regression    
Slug: ridge_regression    
Summary: How to conduct ridge regression in scikit-learn for machine learning in Python.    
Date: 2017-09-18 12:00  
Category: Machine Learning  
Tags: Linear Regression   
Authors: Chris Albon

<a alt="Ridge Regression" href="https://machinelearningflashcards.com">
    <img src="ridge_regression/Ridge_Regression_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.linear_model import Ridge
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
# Create ridge regression with an alpha value
regr = Ridge(alpha=0.5)

# Fit the linear regression
model = regr.fit(X_std, y)
```
