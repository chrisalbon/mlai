Title: Generate Text Reports On Performance  
Slug: generate_text_reports_on_performance  
Summary: How to create generate a text report on a model's performance in scikit-learn for machine learning in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Model Evaluation
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
```

## Load Iris Flower Data


```python
# Load data
iris = datasets.load_iris()

# Create feature matrix
X = iris.data

# Create target vector
y = iris.target

# Create list of target class names
class_names = iris.target_names
```

## Create Training And Test Sets


```python
# Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
```

## Train A Logistic Regression Model


```python
# Create logistic regression
classifier = LogisticRegression()

# Train model and make predictions
y_hat = classifier.fit(X_train, y_train).predict(X_test)
```

## Generate Report


```python
# Create a classification report
print(classification_report(y_test, y_hat, target_names=class_names))
```

                 precision    recall  f1-score   support
    
         setosa       1.00      1.00      1.00        13
     versicolor       1.00      0.62      0.77        16
      virginica       0.60      1.00      0.75         9
    
    avg / total       0.91      0.84      0.84        38
    


Note: Support refers to the number of observations in each class.
