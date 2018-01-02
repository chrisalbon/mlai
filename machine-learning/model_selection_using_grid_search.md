Title: Model Selection Using Grid Search  
Slug: model_selection_tuning_using_grid_search  
Summary: How to conduct grid search for model selection in scikit-learn for machine learning in Python. 
Date: 2017-09-18 12:00  
Category: Machine Learning  
Tags: Model Selection
Authors: Chris Albon

<a alt="Model Selection Using Grid Search" href="https://machinelearningflashcards.com">
    <img src="model_selection_tuning_using_grid_search/Model_Selection_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

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

## Create Pipeline With Model Selection Search Space

Notice that we include both multiple possible learning algorithms _and_ multiple possible hyperparameter values to search over.


```python
# Create a pipeline
pipe = Pipeline([('classifier', RandomForestClassifier())])

# Create space of candidate learning algorithms and their hyperparameters
search_space = [{'classifier': [LogisticRegression()],
                 'classifier__penalty': ['l1', 'l2'],
                 'classifier__C': np.logspace(0, 4, 10)},
                {'classifier': [RandomForestClassifier()],
                 'classifier__n_estimators': [10, 100, 1000],
                 'classifier__max_features': [1, 2, 3]}]
```

## Create Model Selection Using Grid Search


```python
# Create grid search 
clf = GridSearchCV(pipe, search_space, cv=5, verbose=0)
```

## Conduct Model Selection Using Grid Search


```python
# Fit grid search
best_model = clf.fit(X, y)
```

## View Best Model And Its Best Hyperparameters


```python
# View best model
best_model.best_estimator_.get_params()['classifier']
```




    LogisticRegression(C=7.7426368268112693, class_weight=None, dual=False,
              fit_intercept=True, intercept_scaling=1, max_iter=100,
              multi_class='ovr', n_jobs=1, penalty='l1', random_state=None,
              solver='liblinear', tol=0.0001, verbose=0, warm_start=False)



## Predict Using Best Model


```python
# Predict target vector
best_model.predict(X)
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])


