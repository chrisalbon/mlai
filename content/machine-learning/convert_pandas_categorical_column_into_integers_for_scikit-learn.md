Title: Convert Pandas Categorical Data For Scikit-Learn  
Slug: convert_pandas_categorical_column_into_integers_for_scikit-learn  
Summary: Convert Pandas Categorical Column Into Integers For Scikit-Learn  
Date: 2016-11-30 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon  

## Preliminaries


```python
# Import required packages
from sklearn import preprocessing
import pandas as pd
```

## Create DataFrame


```python
raw_data = {'patient': [1, 1, 1, 2, 2],
        'obs': [1, 2, 3, 1, 2],
        'treatment': [0, 1, 0, 1, 0],
        'score': ['strong', 'weak', 'normal', 'weak', 'strong']}
df = pd.DataFrame(raw_data, columns = ['patient', 'obs', 'treatment', 'score'])
```

## Fit The Label Encoder


```python
# Create a label (category) encoder object
le = preprocessing.LabelEncoder()
```


```python
# Fit the encoder to the pandas column
le.fit(df['score'])
```




    LabelEncoder()



## View The Labels


```python
# View the labels (if you want)
list(le.classes_)
```




    ['normal', 'strong', 'weak']



## Transform Categories Into Integers


```python
# Apply the fitted encoder to the pandas column
le.transform(df['score']) 
```




    array([1, 2, 0, 2, 1])



## Transform Integers Into Categories


```python
# Convert some integers into their category names
list(le.inverse_transform([2, 2, 1]))
```




    ['weak', 'weak', 'strong']


