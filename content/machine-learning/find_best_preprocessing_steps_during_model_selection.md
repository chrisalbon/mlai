Title: Find Best Preprocessing Steps During Model Selection  
Slug: find_best_preprocessing_steps_during_model_selection  
Summary: How to conduct preprocessing during model selection in scikit-learn for machine learning in Python. 
Date: 2017-09-18 12:00  
Category: Machine Learning  
Tags: Model Selection
Authors: Chris Albon

We have to be careful to properly handle preprocessing when conducting model selection. First, `GridSearchCV` uses cross-validation to determine which model has the highest performance. However, in cross-validation we are in effect pretending that the fold held out as the test set is not seen, and thus not part of fitting any preprocessing steps (e.g. scaling or standardization). For this reason, we cannot preprocess the data then run `GridSearchCV`.

Second, some preprocessing methods have their own parameter which often have to be supplied by the user. By including candidate component values in the search space, they are treated like any other hyperparameter be to searched over.

## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Set random seed
np.random.seed(0)
```

## Load Iris Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Create Proprocessing Object

We are include two different preprocessing steps: principal component analysis and a k-best feature selection.


```python
# Create a combined preprocessing object
preprocess = FeatureUnion([('pca', PCA()), ("kbest", SelectKBest(k=1))])
```

## Create Pipeline


```python
# Create a pipeline
pipe = Pipeline([('preprocess', preprocess), ('classifier', LogisticRegression())])
```

## Create Search Space Of Hyperparameter Values


```python
# Create space of candidate values
search_space = [{'preprocess__pca__n_components': [1, 2, 3],
                 'classifier__penalty': ['l1', 'l2'],
                 'classifier__C': np.logspace(0, 4, 10)}]
```

## Create Grid Search


```python
# Create grid search 
clf = GridSearchCV(pipe, search_space, cv=5, verbose=0, n_jobs=-1)
```

## Conduct Grid Search


```python
# Fit grid search
best_model = clf.fit(X, y)
```

## View Best Model's Hyperparamters


```python
# View best hyperparameters
print('Best Number Of Princpal Components:', best_model.best_estimator_.get_params()['preprocess__pca__n_components'])
print('Best Penalty:', best_model.best_estimator_.get_params()['classifier__penalty'])
print('Best C:', best_model.best_estimator_.get_params()['classifier__C'])
```

    Best Number Of Princpal Components: 3
    Best Penalty: l1
    Best C: 59.9484250319

