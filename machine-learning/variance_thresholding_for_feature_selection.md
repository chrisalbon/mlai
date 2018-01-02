Title: Variance Thresholding For Feature Selection  
Slug: variance_thresholding_for_feature_selection  
Summary: How to select the best features for machine learning using variance thresholding in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Feature Selection
Authors: Chris Albon

<a alt="Variance Thresholding For Feature Selection" href="https://machinelearningflashcards.com">
    <img src="variance_thresholding_for_feature_selection/Variance_Thresholding_For_Feature_Selection_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
from sklearn import datasets
from sklearn.feature_selection import VarianceThreshold
```

## Load Data


```python
# Load iris data
iris = datasets.load_iris()

# Create features and target
X = iris.data
y = iris.target
```

## Conduct Variance Thresholding


```python
# Create VarianceThreshold object with a variance with a threshold of 0.5
thresholder = VarianceThreshold(threshold=.5)

# Conduct variance thresholding
X_high_variance = thresholder.fit_transform(X)
```

## View high variance features


```python
# View first five rows with features with variances above threshold
X_high_variance[0:5]
```




    array([[ 5.1,  1.4,  0.2],
           [ 4.9,  1.4,  0.2],
           [ 4.7,  1.3,  0.2],
           [ 4.6,  1.5,  0.2],
           [ 5. ,  1.4,  0.2]])


