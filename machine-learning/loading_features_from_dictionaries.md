Title: Loading Features From Dictionaries  
Slug: loading_features_from_dictionaries   
Summary: Loading Features From Dictionaries  
Date: 2016-11-01 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon   

## Preliminaries


```python
from sklearn.feature_extraction import DictVectorizer
```

## Create A Dictionary


```python
staff = [{'name': 'Steve Miller', 'age': 33.},
         {'name': 'Lyndon Jones', 'age': 12.},
         {'name': 'Baxter Morth', 'age': 18.}]
```

## Convert Dictionary To Feature Matrix


```python
# Create an object for our dictionary vectorizer
vec = DictVectorizer()
```


```python
# Fit then transform the staff dictionary with vec, then output an array
vec.fit_transform(staff).toarray()
```




    array([[ 33.,   0.,   0.,   1.],
           [ 12.,   0.,   1.,   0.],
           [ 18.,   1.,   0.,   0.]])



## View Feature Names


```python
# Get Feature Names
vec.get_feature_names()
```




    ['age', 'name=Baxter Morth', 'name=Lyndon Jones', 'name=Steve Miller']


