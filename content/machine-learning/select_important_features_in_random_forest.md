Title: Select Important Features In Random Forest  
Slug: select_important_features_in_random_forest  
Summary: How to select important features in random forest in scikit-learn.  
Date: 2017-09-21 12:00  
Category: Machine Learning  
Tags: Trees And Forests  
Authors: Chris Albon  

## Preliminaries


```python
# Load libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.feature_selection import SelectFromModel
```

## Load Iris Flower Data


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Create Random Forest Classifier


```python
# Create random forest classifier
clf = RandomForestClassifier(random_state=0, n_jobs=-1)
```

## Select Features With Importance Greater Than Threshold

The higher the number, the more important the feature (all importance scores sum to one). By plotting these values we can add interpretability to our random forest models.


```python
# Create object that selects features with importance greater than or equal to a threshold
selector = SelectFromModel(clf, threshold=0.3)

# Feature new feature matrix using selector
X_important = selector.fit_transform(X, y)
```

## View Selected Important Features


```python
# View first five observations of the features
X_important[0:5]
```




    array([[ 1.4,  0.2],
           [ 1.4,  0.2],
           [ 1.3,  0.2],
           [ 1.5,  0.2],
           [ 1.4,  0.2]])



## Train Model With Selected Important Features


```python
# Train random forest using most important featres
model = clf.fit(X_important, y)
```
