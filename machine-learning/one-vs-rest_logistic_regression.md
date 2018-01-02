Title: One Vs. Rest Logistic Regression  
Slug: one-vs-rest_logistic_regression  
Summary: How to train a one-vs-rest logistic regression in scikit-learn.  
Date: 2017-09-21 12:00  
Category: Machine Learning  
Tags: Logistic Regression  
Authors: Chris Albon  

On their own, logistic regressions are only binary classifiers, meaning they cannot handle target vectors with more than two classes. However, there are clever extensions to logistic regression to do just that. In one-vs-rest logistic regression (OVR) a separate model is trained for each class predicted whether an observation is that class or not (thus making it a binary classification problem). It assumes that each classification problem (e.g. class 0 or not) is independent.

## Preliminaries


```python
# Load libraries
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
```

## Load Iris Flower Data


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Standardize Features


```python
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
```

## Create One-Vs-Rest Logistic Regression


```python
# Create one-vs-rest logistic regression object
clf = LogisticRegression(random_state=0, multi_class='ovr')
```

## Train One-Vs-Rest Logistic Regression


```python
# Train model
model = clf.fit(X_std, y)
```

## Create Previously Unseen Observation


```python
# Create new observation
new_observation = [[.5, .5, .5, .5]]
```

## Predict Observation's Class


```python
# Predict class
model.predict(new_observation)
```




    array([2])



## View Probability Observation Is Each Class


```python
# View predicted probabilities
model.predict_proba(new_observation)
```




    array([[ 0.0829087 ,  0.29697265,  0.62011865]])


