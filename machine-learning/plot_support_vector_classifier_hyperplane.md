Title: Plot The Support Vector Classifier's Hyperplane    
Slug: plot_support_vector_classifier_hyperplane   
Summary: How to plot the support vector classifier's hyperplane in Scikit-Learn   
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Support Vector Machines  
Authors: Chris Albon  

<a alt="Support Vector Classifier" href="https://machinelearningflashcards.com">
    <img src="support_vector_classifier/Support_Vector_Classifier_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.svm import LinearSVC
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
from matplotlib import pyplot as plt
```

## Load Iris Flower Data


```python
# Load data with only two classes and two features
iris = datasets.load_iris()
X = iris.data[:100,:2]
y = iris.target[:100]
```

## Standardize Features


```python
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
```

## Train Support Vector Classifier


```python
# Create support vector classifier
svc = LinearSVC(C=1.0)

# Train model
model = svc.fit(X_std, y)
```

## Plot Decision Boundary Hyperplane

In this visualization, all observations of class 0 are black and observations of class 1 are light gray. The hyperplane is the decision-boundary deciding how new observations are classified. Specifically, any observation above the line will by classified as class 0 while any observation below the line will be classified as class 1.


```python
# Plot data points and color using their class
color = ['black' if c == 0 else 'lightgrey' for c in y]
plt.scatter(X_std[:,0], X_std[:,1], c=color)

# Create the hyperplane
w = svc.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-2.5, 2.5)
yy = a * xx - (svc.intercept_[0]) / w[1]

# Plot the hyperplane
plt.plot(xx, yy)
plt.axis("off"), plt.show();
```


![png](plot_support_vector_classifier_hyperplane_files/plot_support_vector_classifier_hyperplane_11_0.png)

