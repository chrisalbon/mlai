Title: Titanic Competition With Random Forest
Slug: titanic_competition_with_random_forest  
Summary: Python code to make a submission to the titanic competition using a random forest.   
Date: 2016-12-29 00:01  
Category: Machine Learning  
Tags: Trees And Forests  
Authors: Chris Albon

This was my first attempt at a Kaggle submission and conducted mostly to understand the Kaggle competition process.

## Preliminaries


```python
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
import csv as csv
```

## Get The Data

You can get the data on [Kaggle's site](https://www.kaggle.com/c/titanic).


```python
# Load the data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
```

## Data Cleaning


```python
# Create a list of the features we will eventually want for our model
features = ['Age', 'SibSp','Parch','Fare','male','embarked_Q','embarked_S','Pclass_2', 'Pclass_3']
```

### Sex

Here we convert the gender labels (`male`, `female`) into a dummy variable (`1`, `0`).


```python
# Create an encoder
sex_encoder = preprocessing.LabelEncoder()

# Fit the encoder to the train data so it knows that male = 1
sex_encoder.fit(train['Sex'])

# Apply the encoder to the training data
train['male'] = sex_encoder.transform(train['Sex'])

# Apply the encoder to the training data
test['male'] = sex_encoder.transform(test['Sex'])
```

### Embarked


```python
# Convert the Embarked training feature into dummies using one-hot
# and leave one first category to prevent perfect collinearity
train_embarked_dummied = pd.get_dummies(train["Embarked"], prefix='embarked', drop_first=True)

# Convert the Embarked test feature into dummies using one-hot
# and leave one first category to prevent perfect collinearity
test_embarked_dummied = pd.get_dummies(test["Embarked"], prefix='embarked', drop_first=True)

# Concatenate the dataframe of dummies with the main dataframes
train = pd.concat([train, train_embarked_dummied], axis=1)
test = pd.concat([test, test_embarked_dummied], axis=1)
```

### Social Class


```python
# Convert the Pclass training feature into dummies using one-hot
# and leave one first category to prevent perfect collinearity
train_Pclass_dummied = pd.get_dummies(train["Pclass"], prefix='Pclass', drop_first=True)

# Convert the Pclass test feature into dummies using one-hot
# and leave one first category to prevent perfect collinearity
test_Pclass_dummied = pd.get_dummies(test["Pclass"], prefix='Pclass', drop_first=True)

# Concatenate the dataframe of dummies with the main dataframes
train = pd.concat([train, train_Pclass_dummied], axis=1)
test = pd.concat([test, test_Pclass_dummied], axis=1)
```

## Impute Missing Values

A number of values of the `Age` feature are missing and will prevent the random forest to train. We get around this we will fill in missing values with the mean value of age (a useful fiction).

### Age


```python
# Create an imputer object
age_imputer = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)

# Fit the imputer object on the training data
age_imputer.fit(train['Age'].reshape(-1, 1))

# Apply the imputer object to the training and test data
train['Age'] = age_imputer.transform(train['Age'].reshape(-1, 1))
test['Age'] = age_imputer.transform(test['Age'].reshape(-1, 1))
```

### Fare


```python
# Create an imputer object
fare_imputer = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)

# Fit the imputer object on the training data
fare_imputer.fit(train['Fare'].reshape(-1, 1))

# Apply the imputer object to the training and test data
train['Fare'] = fare_imputer.transform(train['Fare'].reshape(-1, 1))
test['Fare'] = fare_imputer.transform(test['Fare'].reshape(-1, 1))
```

## Search For Optimum Parameters


```python
# Create a dictionary containing all the candidate values of the parameters
parameter_grid = dict(n_estimators=list(range(1, 5001, 1000)),
                      criterion=['gini','entropy'],
                      max_features=list(range(1, len(features), 2)),
                      max_depth= [None] + list(range(5, 25, 1)))

# Creata a random forest object
random_forest = RandomForestClassifier(random_state=0, n_jobs=-1)

# Create a gridsearch object with 5-fold cross validation, and uses all cores (n_jobs=-1)
clf = GridSearchCV(estimator=random_forest, param_grid=parameter_grid, cv=5, verbose=1, n_jobs=-1)
```


```python
# Nest the gridsearchCV in a 3-fold CV for model evaluation
cv_scores = cross_val_score(clf, train[features], train['Survived'])

# Print results
print('Accuracy scores:', cv_scores)
print('Mean of score:', np.mean(cv_scores))
print('Variance of scores:', np.var(cv_scores))
```

## Retrain The Random Forest With The Optimum Parameters


```python
# Retrain the model on the whole dataset
clf.fit(train[features], train['Survived'])

# Predict who survived in the test dataset
predictions = clf.predict(test[features])
```

## Create The Kaggle Submission


```python
# Grab the passenger IDs
ids = test['PassengerId'].values

# Create a csv
submission_file = open("submission.csv", "w")

# Write to that csv
open_file_object = csv.writer(submission_file)

# Write the header of the csv
open_file_object.writerow(["PassengerId","Survived"])

# Write the rows of the csv
open_file_object.writerows(zip(ids, predictions))

# Close the file
submission_file.close()
```
