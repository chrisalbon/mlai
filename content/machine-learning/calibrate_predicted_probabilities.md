Title: Calibrate Predicted Probabilities    
Slug: calibrate_predicted_probabilities   
Summary: How to calibrate predicted probabilities of naive bayes classifer in Scikit-Learn   
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Naive Bayes     
Authors: Chris Albon  

Class probabilities are a common and useful part of machine learning models. In scikit-learn, most learning algortihms allow us to see the predicted probabilities of class membership using `predict_proba`. This can be extremely useful if, for instance, we want to only predict a certain class if the model predicts the probability that they are that class is over 90%. However, some models, including naive Bayes classifiers output probabilities that are not based on the real world. That is, `predict_proba` might predict an observation has a 0.70 chance of being a certain class, when the reality is that it is 0.10 or 0.99. Specifically in naive Bayes, while the ranking of predicted probabilities for the different target classes is valid, the raw predicted probabilities tend to take on extreme values close to 0 and 1. 

To obtain meaningful predicted probabilities we need conduct what is called calibration. In scikit-learn we can use the `CalibratedClassifierCV` class to create well calibrated predicted probabilities using k-fold cross-validation. In `CalibratedClassifierCV` the training sets are used to train the model and the test sets is used to calibrate the predicted probabilities. The returned predicted probabilities are the average of the k-folds.

## Preliminaries


```python
# Load libraries
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.calibration import CalibratedClassifierCV
```

## Load Iris Flower Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Create Naive Bayes Classifier


```python
# Create Gaussian Naive Bayes object
clf = GaussianNB()
```

## Create Calibrator


```python
# Create calibrated cross-validation with sigmoid calibration
clf_sigmoid = CalibratedClassifierCV(clf, cv=2, method='sigmoid')
```

## Create Classifier With Calibrated Probabilities


```python
# Calibrate probabilities
clf_sigmoid.fit(X, y)
```




    CalibratedClassifierCV(base_estimator=GaussianNB(priors=None), cv=2,
                method='sigmoid')



## Create Previously Unseen Observation


```python
# Create new observation
new_observation = [[ 2.6,  2.6,  2.6,  0.4]]
```

## View Calibrated Probabilities


```python
# View calibrated probabilities
clf_sigmoid.predict_proba(new_observation)
```




    array([[ 0.31859969,  0.63663466,  0.04476565]])


