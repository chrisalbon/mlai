Title: Calibrate Predicted Probabilities In SVC    
Slug: calibrate_predicted_probabilities_in_svc   
Summary: How to calibrate predicted probabilities in support vector classifier in Scikit-Learn   
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Support Vector Machines  
Authors: Chris Albon  

SVC's use of a hyperplane to create decision regions do not naturally output a probability estimate that an observation is a member of a certain class. However, we can in fact output calibrated class probabilities with a few caveats. In an SVC, Platt scaling can be used, wherein first the SVC is trained, then a separate cross-validated logistic regression is trained to map the SVC outputs into probabilities:

$$P(y=1 \mid x)={\frac {1}{1+e^{(A*f(x)+B)}}}$$

where $A$ and $B$ are parameter vectors and $f$ is the $i$th observation's signed distance from the hyperplane. When we have more than two classes, an extension of Platt scaling is used.

In scikit-learn, the predicted probabilities must be generated when the model is being trained. This can be done by setting `SVC`'s `probability` to `True`. After the model is trained, we can output the estimated probabilities for each class using `predict_proba`.

## Preliminaries


```python
# Load libraries
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
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

## Train Support Vector Classifier


```python
# Create support vector classifier object
svc = SVC(kernel='linear', probability=True, random_state=0)

# Train classifier
model = svc.fit(X_std, y)
```

## Create Previously Unseen Observation


```python
# Create new observation
new_observation = [[.4, .4, .4, .4]]
```

## View Predicted Probabilities


```python
# View predicted probabilities
model.predict_proba(new_observation)
```




    array([[ 0.00588822,  0.96874828,  0.0253635 ]])


