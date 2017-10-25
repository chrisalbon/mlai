Title: Create Baseline Classification Model  
Slug: create_baseline_classification_model  
Summary: How to create a baseline classification model in scikit-learn for machine learning in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Model Evaluation   
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
```

## Load Iris Flower Dataset


```python
# Load data
iris = load_iris()

# Create target vector and feature matrix
X, y = iris.data, iris.target
```

## Split Data Into Training And Test Set


```python
# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

## Create Dummy Regression Always Predicts The Mean Value Of Target


```python
# Create dummy classifer
dummy = DummyClassifier(strategy='uniform', random_state=1)

# "Train" model
dummy.fit(X_train, y_train)
```




    DummyClassifier(constant=None, random_state=1, strategy='uniform')



## Evaluate Performance Metric


```python
# Get accuracy score
dummy.score(X_test, y_test)  
```




    0.42105263157894735


