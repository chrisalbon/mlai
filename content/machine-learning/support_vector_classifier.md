Title: Support Vector Classifier    
Slug: support_vector_classifier   
Summary: How to train a support vector classifier in Scikit-Learn   
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Support Vector Machines  
Authors: Chris Albon  

<a alt="Support Vector Classifier" href="https://machinelearningflashcards.com">
    <img src="support_vector_classifier/Support_Vector_Classifier_print.png" class="flashcard center-block">
</a>

There is a balance between SVC maximizing the margin of the hyperplane and minimizing the misclassification. In SVC, the later is controlled with the hyperparameter $C$, the penalty imposed on errors. C is a parameter of the SVC learner and is the penalty for misclassifying a data point. When C is small, the classifier is okay with misclassified data points (high bias but low variance). When C is large, the classifier is heavily penalized for misclassified data and therefore bends over backwards avoid any misclassified data points (low bias but high variance).

In scikit-learn, $C$ is determined by the parameter `C` and defaults to `C=1.0`. We should treat $C$ has a hyperparameter of our learning algorithm which we tune using model selection techniques.

## Preliminaries


```python
# Load libraries
from sklearn.svm import LinearSVC
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
```

## Load Iris Flower Data


```python
# Load feature and target data
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

## Train Support Vector Classifier


```python
# Create support vector classifier
svc = LinearSVC(C=1.0)

# Train model
model = svc.fit(X_std, y)
```

## Create Previously Unseen Observation


```python
# Create new observation
new_observation = [[-0.7, 1.1, -1.1 , -1.7]]
```

## Predict Class Of Observation


```python
# Predict class of new observation
svc.predict(new_observation)
```




    array([0])


