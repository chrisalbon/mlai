Title: Logistic Regression With L1 Regularization  
Slug: logistic_regression_with_l1_regularization  
Summary: Logistic Regression With L1 Regularization using scikit-learn.  
Date: 2016-12-01 12:00  
Category: Machine Learning  
Tags: Logistic Regression  
Authors: Chris Albon  

L1 regularization (also called least absolute deviations) is a powerful tool in data science. There are many tutorials out there explaining L1 regularization and I will not try to do that here. Instead, this tutorial is show the effect of the regularization parameter `C` on the coefficients and model accuracy.

## Preliminaries


```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
```

## Create The Data

The dataset used in this tutorial is the famous [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set). The Iris target data contains 50 samples from three species of Iris, `y` and four feature variables, `X`.

The dataset contains three categories (three species of Iris), however for the sake of simplicity it is easier if the target data is binary. Therefore we will remove the data from the last species of Iris.


```python
# Load the iris dataset
iris = datasets.load_iris()

# Create X from the features
X = iris.data

# Create y from output
y = iris.target

# Remake the variable, keeping all data where the category is not 2.
X = X[y != 2]
y = y[y != 2]
```

## View The Data


```python
# View the features
X[0:5]
```




    array([[ 5.1,  3.5,  1.4,  0.2],
           [ 4.9,  3. ,  1.4,  0.2],
           [ 4.7,  3.2,  1.3,  0.2],
           [ 4.6,  3.1,  1.5,  0.2],
           [ 5. ,  3.6,  1.4,  0.2]])




```python
# View the target data
y
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1])



## Split The Data Into Training And Test Sets


```python
# Split the data into test and training sets, with 30% of samples being put into the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
```

## Standardize Features

Because the regularization penalty is comprised of the sum of the absolute value of the coefficients, we need to scale the data so the coefficients are all based on the same scale.


```python
# Create a scaler object
sc = StandardScaler()

# Fit the scaler to the training data and transform
X_train_std = sc.fit_transform(X_train)

# Apply the scaler to the test data
X_test_std = sc.transform(X_test)
```

## Run Logistic Regression With A L1 Penalty With Various Regularization Strengths

The usefulness of L1 is that it can push feature coefficients to 0, creating a method for feature selection. In the code below we run a logistic regression with a L1 penalty four times, each time decreasing the value of `C`. We should expect that as `C` decreases, more coefficients become 0.


```python
C = [10, 1, .1, .001]

for c in C:
    clf = LogisticRegression(penalty='l1', C=c)
    clf.fit(X_train, y_train)
    print('C:', c)
    print('Coefficient of each feature:', clf.coef_)
    print('Training accuracy:', clf.score(X_train, y_train))
    print('Test accuracy:', clf.score(X_test, y_test))
    print('')
```

    C: 10
    Coefficient of each feature: [[-0.0855264  -3.75409972  4.40427765  0.        ]]
    Training accuracy: 1.0
    Test accuracy: 1.0
    
    C: 1
    Coefficient of each feature: [[ 0.         -2.28800472  2.5766469   0.        ]]
    Training accuracy: 1.0
    Test accuracy: 1.0
    
    C: 0.1
    Coefficient of each feature: [[ 0.         -0.82310456  0.97171847  0.        ]]
    Training accuracy: 1.0
    Test accuracy: 1.0
    
    C: 0.001
    Coefficient of each feature: [[ 0.  0.  0.  0.]]
    Training accuracy: 0.5
    Test accuracy: 0.5
    


Notice that as `C` decreases the model coefficients become smaller (for example from `4.36276075` when `C=10` to `0.0.97175097` when `C=0.1`), until at `C=0.001` all the coefficients are zero. This is the effect of the regularization penalty becoming more prominent.
