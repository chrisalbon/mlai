Title: Decision Tree Classifier  
Slug: decision_tree_classifier  
Summary: Training a decision tree classifier in scikit-learn.  
Date: 2017-09-19 12:00  
Category: Machine Learning  
Tags: Trees And Forests  
Authors: Chris Albon  

<a alt="Gini Index" href="https://machinelearningflashcards.com">
    <img src="decision_tree_classifier/Gini_Index_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
```

## Load Iris Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Create Decision Tree Using Gini Impurity


```python
# Create decision tree classifer object using gini
clf = DecisionTreeClassifier(criterion='gini', random_state=0)
```

## Train Model


```python
# Train model
model = clf.fit(X, y)
```

## Create Observation To Predict


```python
# Make new observation
observation = [[ 5,  4,  3,  2]]
```

## Predict Observation


```python
# Predict observation's class    
model.predict(observation)
```




    array([1])



## View Predicted Probabilities


```python
# View predicted class probabilities for the three classes
model.predict_proba(observation)
```




    array([[ 0.,  1.,  0.]])


