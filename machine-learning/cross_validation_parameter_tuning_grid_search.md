Title: Cross Validation With Parameter Tuning Using Grid Search  
Slug: cross_validation_parameter_tuning_grid_search  
Summary: Cross Validation With Parameter Tuning Using Grid Search using Scikit-Learn.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Model Selection  
Authors: Chris Albon 

In machine learning, two tasks are commonly done at the same time in data pipelines: cross validation and (hyper)parameter tuning. Cross validation is the process of training learners using one set of data and testing it using a different set. Parameter tuning is the process to selecting the values for a model's parameters that maximize the accuracy of the model.

In this tutorial we work through an example which combines cross validation and parameter tuning using scikit-learn.

Note: This tutorial is based on [examples given in the scikit-learn documentation](http://scikit-learn.org/stable/modules/grid_search.html#grid-search). I have combined a few examples in the documentation, simplified the code, and added extensive explanations/code comments.

## Preliminaries


```python
import numpy as np
from sklearn.grid_search import GridSearchCV
from sklearn import datasets, svm
import matplotlib.pyplot as plt
```

## Create Two Datasets

In the code below, we load the [`digits` dataset](http://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html), which contains 64 feature variables. Each feature denotes the darkness of a pixel in an 8 by 8 image of a handwritten digit. We can see these features for the first observation:


```python
# Load the digit data
digits = datasets.load_digits()
```


```python
# View the features of the first observation
digits.data[0:1]
```




    array([[  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.,   0.,   0.,  13.,
             15.,  10.,  15.,   5.,   0.,   0.,   3.,  15.,   2.,   0.,  11.,
              8.,   0.,   0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.,   0.,
              5.,   8.,   0.,   0.,   9.,   8.,   0.,   0.,   4.,  11.,   0.,
              1.,  12.,   7.,   0.,   0.,   2.,  14.,   5.,  10.,  12.,   0.,
              0.,   0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.]])



The target data is a vector containing the image's true digit. For example, the first observation is a handwritten digit for '0'.


```python
# View the target of the first observation
digits.target[0:1]
```




    array([0])



To demonstrate cross validation and parameter tuning, first we are going to divide the digit data into two datasets called `data1` and `data2`. `data1` contains the first 1000 rows of the digits data, while `data2` contains the remaining ~800 rows. Note that this split is _separate_ to the cross validation we will conduct and is done purely to demonstrate something at the end of the tutorial. In other words, don't worry about `data2` for now, we will come back to it.


```python
# Create dataset 1
data1_features = digits.data[:1000]
data1_target = digits.target[:1000]

# Create dataset 2
data2_features = digits.data[1000:]
data2_target = digits.target[1000:]
```

## Create Parameter Candidates

Before looking for which combination of parameter values produces the most accurate model, we must specify the different candidate values we want to try. In the code below we have a number of candidate parameter values, including four different values for `C` (`1, 10, 100, 1000`), two values for `gamma` (`0.001, 0.0001`), and two kernels (`linear, rbf`). The grid search will try all combinations of parameter values and select the set of parameters which provides the most accurate model.


```python
parameter_candidates = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
]
```

## Conduct Grid Search To Find Parameters Producing Highest Score

Now we are ready to conduct the grid search using scikit-learn's `GridSearchCV` which stands for grid search cross validation. By default, the `GridSearchCV`'s cross validation uses 3-fold `KFold` or `StratifiedKFold` depending on the situation.


```python
# Create a classifier object with the classifier and parameter candidates
clf = GridSearchCV(estimator=svm.SVC(), param_grid=parameter_candidates, n_jobs=-1)

# Train the classifier on data1's feature and target data
clf.fit(data1_features, data1_target)   
```




    GridSearchCV(cv=None, error_score='raise',
           estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
      decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
      max_iter=-1, probability=False, random_state=None, shrinking=True,
      tol=0.001, verbose=False),
           fit_params={}, iid=True, n_jobs=-1,
           param_grid=[{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}, {'kernel': ['rbf'], 'gamma': [0.001, 0.0001], 'C': [1, 10, 100, 1000]}],
           pre_dispatch='2*n_jobs', refit=True, scoring=None, verbose=0)



Success! We have our results! First, let's look at the accuracy score when we apply the model to the `data1`'s test data.


```python
# View the accuracy score
print('Best score for data1:', clf.best_score_) 
```

    Best score for data1: 0.942


Which parameters are the best? We can tell scikit-learn to display them:


```python
# View the best parameters for the model found using grid search
print('Best C:',clf.best_estimator_.C) 
print('Best Kernel:',clf.best_estimator_.kernel)
print('Best Gamma:',clf.best_estimator_.gamma)
```

    Best C: 10
    Best Kernel: rbf
    Best Gamma: 0.001


This tells us that the most accurate model uses `C=10`, the `rbf` kernel, and `gamma=0.001`.

## Sanity Check Using Second Dataset

Remember the second dataset we created? Now we will use it to prove that those parameters are actually used by the model. First, we apply the classifier we just trained to the second dataset. Then we will train a _new_ support vector classifier from scratch using the parameters found using the grid search. We should get the same results for both models.


```python
# Apply the classifier trained using data1 to data2, and view the accuracy score
clf.score(data2_features, data2_target)  
```




    0.96988707653701378




```python
# Train a new classifier using the best parameters found by the grid search
svm.SVC(C=10, kernel='rbf', gamma=0.001).fit(data1_features, data1_target).score(data2_features, data2_target)
```




    0.96988707653701378



Success!
