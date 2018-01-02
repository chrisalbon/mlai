Title: Imbalanced Classes In SVM    
Slug: imbalanced_classes_in_svm   
Summary: How to handle imbalanced classes in support vector machines in Scikit-Learn   
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Support Vector Machines  
Authors: Chris Albon  

In support vector machines, $C$ is a hyperparameter determining the penalty for misclassifying an observation. One method for handling imbalanced classes in support vector machines is to weight $C$ by classes, so that

$$C_k = C * w_j$$

where $C$ is the penalty for misclassification, $w_j$ is a weight inversely proportional to class $j$'s frequency, and $C_j$ is the $C$ value for class $j$. The general idea is to increase the penalty for misclassifying minority classes to prevent them from being "overwhelmed" by the majority class.

In scikit-learn, when using `SVC` we can set the values for $C_j$ automatically by setting `class_weight='balanced'`
The `balanced` argument automatically weighs classes such that:

$$w_j = \frac{n}{kn_{j}}$$

where $w_j$ is the weight to class $j$, $n$ is the number of observations, $n_j$ is the number of observations in class $j$, and $k$ is the total number of classes.

## Preliminaries


```python
# Load libraries
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
```

## Load Iris Flower Dataset


```python
#Load data with only two classes
iris = datasets.load_iris()
X = iris.data[:100,:]
y = iris.target[:100]
```

## Imbalanced Iris Flower Classes


```python
# Make class highly imbalanced by removing first 40 observations
X = X[40:,:]
y = y[40:]

# Create target vector indicating if class 0, otherwise 1
y = np.where((y == 0), 0, 1)
```

## Standardize Features


```python
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
```

## Train Support Vector Classifier With Weighted Classes


```python
# Create support vector classifier
svc = SVC(kernel='linear', class_weight='balanced', C=1.0, random_state=0)

# Train classifier
model = svc.fit(X_std, y)
```
