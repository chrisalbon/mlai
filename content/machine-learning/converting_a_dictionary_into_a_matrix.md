Title: Converting A Dictionary Into A Matrix  
Slug: converting_a_dictionary_into_a_matrix 
Summary: How to convert a dictionary into a feature matrix for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

## Preliminaries


```python
# Load library
from sklearn.feature_extraction import DictVectorizer
```

## Create Dictionary


```python
# Our dictionary of data
data_dict = [{'Red': 2, 'Blue': 4},
             {'Red': 4, 'Blue': 3},
             {'Red': 1, 'Yellow': 2},
             {'Red': 2, 'Yellow': 2}]
```

## Feature Matrix From Dictionary


```python
# Create DictVectorizer object
dictvectorizer = DictVectorizer(sparse=False)

# Convert dictionary into feature matrix
features = dictvectorizer.fit_transform(data_dict)

# View feature matrix
features
```




    array([[ 4.,  2.,  0.],
           [ 3.,  4.,  0.],
           [ 0.,  1.,  2.],
           [ 0.,  2.,  2.]])



## View column names


```python
# View feature matrix column names
dictvectorizer.get_feature_names()
```




    ['Blue', 'Red', 'Yellow']


