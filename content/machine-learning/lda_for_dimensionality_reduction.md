Title: Using Linear Discriminant Analysis For Dimensionality Reduction   
Slug: lda_for_dimensionality_reduction   
Summary: How to use linear discriminant analysis for dimensionality reduction using Python.   
Date: 2017-09-13 12:00   
Category: Machine Learning   
Tags: Feature Engineering  
Authors: Chris Albon   

## Preliminaries


```python
# Load libraries
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
```

## Load Iris Data


```python
# Load the Iris flower dataset:
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Create A Linear 


```python
# Create an LDA that will reduce the data down to 1 feature
lda = LinearDiscriminantAnalysis(n_components=1)

# run an LDA and use it to transform the features
X_lda = lda.fit(X, y).transform(X)
```

## View Results


```python
# Print the number of features
print('Original number of features:', X.shape[1])
print('Reduced number of features:', X_lda.shape[1])
```

    Original number of features: 4
    Reduced number of features: 1


## View Percentage Of Variance Retained By New Features


```python
## View the ratio of explained variance
lda.explained_variance_ratio_
```




    array([ 0.99147248])


