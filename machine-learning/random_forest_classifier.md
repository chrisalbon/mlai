Title: Random Forest Classifier  
Slug: random_forest_classifier  
Summary: Training a random forest classifier in scikit-learn.  
Date: 2017-09-21 12:00  
Category: Machine Learning  
Tags: Trees And Forests  
Authors: Chris Albon  

## Preliminaries


```python
# Load libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
```

## Load Iris Data


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Create Random Forest Classifier


```python
# Create random forest classifer object that uses entropy
clf = RandomForestClassifier(criterion='entropy', random_state=0, n_jobs=-1)
```

## Train Random Forest Classifier


```python
# Train model
model = clf.fit(X, y)
```

## Predict Previously Unseen Observation


```python
# Make new observation
observation = [[ 5,  4,  3,  2]]
              
# Predict observation's class    
model.predict(observation)
```




    array([1])


