Title: Split Data Into Training And Test Sets  
Slug: split_data_into_training_and_test_sets  
Summary: How to split data into training and test sets for machine learning in Python.    
Date: 2017-09-15 12:00  
Category: Machine Learning  
Tags: Model Evaluation
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
```

## Load Digits Dataset


```python
# Load the digits dataset
digits = datasets.load_digits()

# Create the features matrix
X = digits.data

# Create the target vector
y = digits.target
```

## Split Into Training And Test Sets


```python
# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.1, 
                                                    random_state=1)
```

## Fit Standardizer To Training Set


```python
# Create standardizer
standardizer = StandardScaler()

# Fit standardizer to training set
standardizer.fit(X_train)
```




    StandardScaler(copy=True, with_mean=True, with_std=True)



## Apply Standardizer To Training And Test Sets


```python
# Apply to both training and test sets
X_train_std = standardizer.transform(X_train)
X_test_std = standardizer.transform(X_test)
```
