Title: Handle Imbalanced Classes In Random Forest  
Slug: handle_imbalanced_classes_in_random_forests  
Summary: Handle imbalanced classes in random forests in scikit-learn.  
Date: 2017-09-21 12:00  
Category: Machine Learning  
Tags: Trees And Forests  
Authors: Chris Albon  

## Preliminaries


```python
# Load libraries
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import datasets
```

## Load Iris Flower Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Adjust Iris Dataset To Make Classes Imbalanced


```python
# Make class highly imbalanced by removing first 40 observations
X = X[40:,:]
y = y[40:]

# Create target vector indicating if class 0, otherwise 1
y = np.where((y == 0), 0, 1)
```

## Train Random Forest While Balancing Classes

When using `RandomForestClassifier` a useful setting is `class_weight=balanced` wherein classes are automatically weighted inversely proportional to how frequently they appear in the data. Specifically:

$$w_j = \frac{n}{kn_{j}}$$

where $w_j$ is the weight to class $j$, $n$ is the number of observations, $n_j$ is the number of observations in class $j$, and $k$ is the total number of classes.


```python
# Create decision tree classifer object
clf = RandomForestClassifier(random_state=0, n_jobs=-1, class_weight="balanced")

# Train model
model = clf.fit(X, y)
```
