Title: Custom Performance Metric  
Slug: custom_performance_metric  
Summary: How to create a custom performance metric in scikit-learn for machine learning in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Model Evaluation
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from sklearn.metrics import make_scorer, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression
```

## Create Feature 


```python
# Generate features matrix and target vector
X, y = make_regression(n_samples = 100,
                          n_features = 3,
                          random_state = 1)

# Create training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)
```

## Train model


```python
# Create ridge regression object
classifier = Ridge()

# Train ridge regression model
model = classifier.fit(X_train, y_train)
```

## Create Custom Performance Metric

For this example we are just calculating the r-squared score, but we can see that any calculation can be used.


```python
# Create custom metric
def custom_metric(y_test, y_pred):
    # Calculate r-squared score
    r2 = r2_score(y_test, y_pred)
    # Return r-squared score
    return r2
```

## Make Custom Metric A Scorer Object


```python
# Make scorer and define that higher scores are better
score = make_scorer(custom_metric, greater_is_better=True)
```

## User Scorer To Evaluate Model Performance


```python
# Apply custom scorer to ridge regression
score(model, X_test, y_test)
```




    0.99979061028820582


