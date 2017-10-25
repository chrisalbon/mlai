Title: Loading scikit-learn's Iris Dataset  
Slug: loading_scikit-learns_iris-dataset  
Summary: Loading the built-in Iris datasets of scikit-learn.   
Date: 2016-08-31 12:00  
Category: Machine Learning  
Tags: Basics  
Authors: Chris Albon 

## Preliminaries


```python
# Load libraries
from sklearn import datasets
import matplotlib.pyplot as plt 
```

## Load Iris Dataset

The [Iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) is one of the most famous databases for classification. It contains three classes (i.e. three species of flowers) with 50 observations per class.


```python
# Load digits dataset
iris = datasets.load_iris()

# Create feature matrix
X = iris.data

# Create target vector
y = iris.target

# View the first observation's feature values
X[0]
```




    array([ 5.1,  3.5,  1.4,  0.2])


