Title: Perceptron In Scikit  
Slug: perceptron_in_scikit  
Summary: Perceptron Learning using Python and scikit-learn.  
Date: 2016-11-04 12:00  
Category: Machine Learning  
Tags: Other  
Authors: Chris Albon 

A perceptron learner was one of the earliest machine learning techniques and still from the foundation of many modern neural networks. In this tutorial we use a perceptron learner to classify the [famous iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set). This tutorial was inspired by [Python Machine Learning by Sebastian Raschka](http://amzn.to/2iyMbpA).

## Preliminaries


```python
# Load required libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
```

## Load The Iris Data


```python
# Load the iris dataset
iris = datasets.load_iris()

# Create our X and y data
X = iris.data
y = iris.target
```

## View The Iris Data


```python
# View the first five observations of our y data
y[:5]
```




    array([0, 0, 0, 0, 0])




```python
# View the first five observations of our x data.
# Notice that there are four independent variables (features)
X[:5]
```




    array([[ 5.1,  3.5,  1.4,  0.2],
           [ 4.9,  3. ,  1.4,  0.2],
           [ 4.7,  3.2,  1.3,  0.2],
           [ 4.6,  3.1,  1.5,  0.2],
           [ 5. ,  3.6,  1.4,  0.2]])



## Split The Iris Data Into Training And Test


```python
# Split the data into 70% training data and 30% test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
```

## Preprocess The X Data By Scaling


```python
# Train the scaler, which standarizes all the features to have mean=0 and unit variance
sc = StandardScaler()
sc.fit(X_train)
```




    StandardScaler(copy=True, with_mean=True, with_std=True)




```python
# Apply the scaler to the X training data
X_train_std = sc.transform(X_train)

# Apply the SAME scaler to the X test data
X_test_std = sc.transform(X_test)
```

## Train A Perceptron Learner


```python
# Create a perceptron object with the parameters: 40 iterations (epochs) over the data, and a learning rate of 0.1
ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0)

# Train the perceptron
ppn.fit(X_train_std, y_train)
```




    Perceptron(alpha=0.0001, class_weight=None, eta0=0.1, fit_intercept=True,
          n_iter=40, n_jobs=1, penalty=None, random_state=0, shuffle=True,
          verbose=0, warm_start=False)



## Apply The Trained Learner To Test Data


```python
# Apply the trained perceptron on the X data to make predicts for the y test data
y_pred = ppn.predict(X_test_std)
```

## Compare The Predicted Y With The True Y


```python
# View the predicted y test data
y_pred
```




    array([0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2,
           2, 1, 0, 0, 2, 1, 0, 0, 0, 0, 2, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1])




```python
# View the true y test data
y_test
```




    array([0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 1, 1, 0, 2, 2, 2, 1, 0, 0, 0, 0, 2,
           2, 1, 1, 0, 2, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1])



## Examine Accuracy Metric


```python
# View the accuracy of the model, which is: 1 - (observations predicted wrong / total observations)
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
```

    Accuracy: 0.87

