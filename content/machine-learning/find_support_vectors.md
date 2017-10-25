Title: Find Support Vectors    
Slug: find_support_vectors   
Summary: How to find support vectors in Scikit-Learn   
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Support Vector Machines  
Authors: Chris Albon  

<a alt="Find Support Vectors" href="https://machinelearningflashcards.com">
    <img src="find_support_vectors/Support_Vectors_print.png" class="flashcard center-block">
</a>

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

## Standardize Features


```python
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
```

## Train Support Vector Classifier


```python
# Create support vector classifier object
svc = SVC(kernel='linear', random_state=0)

# Train classifier
model = svc.fit(X_std, y)
```

## View Support Vectors


```python
# View support vectors
model.support_vectors_
```




    array([[-0.5810659 ,  0.43490123, -0.80621461, -0.50581312],
           [-1.52079513, -1.67626978, -1.08374115, -0.8607697 ],
           [-0.89430898, -1.46515268,  0.30389157,  0.38157832],
           [-0.5810659 , -1.25403558,  0.09574666,  0.55905661]])



## View Indices Of Support Vectors


```python
# View indices of support vectors
model.support_
```




    array([23, 41, 57, 98], dtype=int32)



## View Number Of Support Vectors With Each Class


```python
# View number of support vectors for each class
model.n_support_
```




    array([2, 2], dtype=int32)


