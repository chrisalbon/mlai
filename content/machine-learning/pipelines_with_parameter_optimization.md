Title: Pipelines With Parameter Optimization   
Slug: pipelines_with_parameter_optimization  
Summary: Pipelines with parameter optimization using scikit-learn.  
Date: 2016-12-01 12:00  
Category: Machine Learning  
Tags: Model Selection  
Authors: Chris Albon  

## Preliminaries


```python
# Import required packages
import numpy as np
from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
```

## Load Data


```python
# Load the breast cancer data
dataset = datasets.load_breast_cancer()

# Create X from the dataset's features
X = dataset.data

# Create y from the dataset's output
y = dataset.target
```

## Create Pipelines


```python
# Create an scaler object
sc = StandardScaler()

# Create a pca object
pca = decomposition.PCA()

# Create a logistic regression object with an L2 penalty
logistic = linear_model.LogisticRegression()

# Create a pipeline of three steps. First, standardize the data.
# Second, tranform the data with PCA.
# Third, train a logistic regression on the data.
pipe = Pipeline(steps=[('sc', sc), 
                       ('pca', pca), 
                       ('logistic', logistic)])
```

## Create Parameter Space


```python
# Create a list of a sequence of integers from 1 to 30 (the number of features in X + 1)
n_components = list(range(1,X.shape[1]+1,1))

# Create a list of values of the regularization parameter
C = np.logspace(-4, 4, 50)

# Create a list of options for the regularization penalty
penalty = ['l1', 'l2']

# Create a dictionary of all the parameter options 
# Note has you can access the parameters of steps of a pipeline by using '__’
parameters = dict(pca__n_components=n_components, 
                  logistic__C=C,
                  logistic__penalty=penalty)
```

## Conduct Parameter Optmization With Pipeline


```python
# Create a grid search object
clf = GridSearchCV(pipe, parameters)

# Fit the grid search
clf.fit(X, y)
```


```python
# View The Best Parameters
print('Best Penalty:', clf.best_estimator_.get_params()['logistic__penalty'])
print('Best C:', clf.best_estimator_.get_params()['logistic__C'])
print('Best Number Of Components:', clf.best_estimator_.get_params()['pca__n_components'])
```

## Use Cross Validation To Evaluate Model


```python
# Fit the grid search using 3-Fold cross validation
cross_val_score(clf, X, y)
```
