Title: Nested Cross Validation  
Slug: nested_cross_validation  
Summary: Nested Cross Validation using scikit-learn.  
Date: 2016-12-02 12:00  
Category: Machine Learning  
Tags: Model Evaluation  
Authors: Chris Albon  

Often we want to tune the parameters of a model (for example, `C` in a support vector machine). That is, we want to find the value of a parameter that minimizes our loss function. The best way to do this is cross validation: 

1. Set the parameter you want to tune to some value.
2. Split your data into K 'folds' (sections).
3. Train your model using K-1 folds using the parameter value.
4. Test your model on the remaining fold.
5. Repeat steps 3 and 4 so that every fold is the test data once. 
6. Repeat steps 1 to 5 for every possible value of the parameter.
7. Report the parameter that produced the best result.

However, as [Cawley and Talbot](http://jmlr.org/papers/volume11/cawley10a/cawley10a.pdf) point out in their 2010 paper, since we used the test set to _both_ select the values of the parameter _and_ evaluate the model, we risk optimistically biasing our model evaluations. For this reason, if a test set is used to select model parameters, then we need a _different_ test set to get an unbiased evaluation of that selected model.

One way to overcome this problem is to have nested cross validations. First, an inner cross validation is used to tune the parameters and select the best model. Second, an outer cross validation is used to evaluate the model selected by the inner cross validation.

## Preliminaries


```python
# Load required packages
from sklearn import datasets
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.svm import SVC
```

## Get Data

The data for this tutorial is beast cancer data with [30 features and a binary target variable](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html).


```python
# Load the data
dataset = datasets.load_breast_cancer()

# Create X from the features
X = dataset.data

# Create y from the target
y = dataset.target
```

## Standardize Data


```python
# Create a scaler object
sc = StandardScaler()

# Fit the scaler to the feature data and transform
X_std = sc.fit_transform(X)
```

## Create Inner Cross Validation (For Parameter Tuning)

This is our inner cross validation. We will use this to hunt for the best parameters for `C`, the penalty for misclassifying a data point. `GridSearchCV` will conduct steps 1-6 listed at the top of this tutorial.


```python
# Create a list of 10 candidate values for the C parameter
C_candidates = dict(C=np.logspace(-4, 4, 10))

# Create a gridsearch object with the support vector classifier and the C value candidates
clf = GridSearchCV(estimator=SVC(), param_grid=C_candidates)
```

The code below isn't necessary for parameter tuning using nested cross validation, however to demonstrate that our inner cross validation grid search can find the best value for the parameter `C`, we will run it once here:


```python
# Fit the cross validated grid search on the data 
clf.fit(X_std, y)

# Show the best value for C
clf.best_estimator_.C
```




    2.7825594022071258



## Create Outer Cross Validation (For Model Evaluation)

With our inner cross validation constructed, we can use `cross_val_score` to evaluate the model with a second (outer) cross validation. 

The code below splits the data into three folds, running the inner cross validation on two of the folds (merged together) and then evaluating the model on the third fold. This is repeated three times so that every fold is used for testing once.


```python
cross_val_score(clf, X_std, y)
```




    array([ 0.94736842,  0.97894737,  0.98412698])



Each the values above is an unbiased evaluation of the model's accuracy, once for each of the three test folds. Averaged together, they would represent the average accuracy of the model found in the inner cross validated grid search.
