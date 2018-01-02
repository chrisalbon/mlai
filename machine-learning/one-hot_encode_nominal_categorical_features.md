Title: One-Hot Encode Nominal Categorical Features  
Slug: one-hot_encode_nominal_categorical_features     
Summary: How to one-hot encode nominal categorical features for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

<a alt="One-hot encoding" href="https://machinelearningflashcards.com">
    <img src="one-hot_encode_nominal_categorical_features/One-Hot_Encoding_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.preprocessing import LabelBinarizerr
import numpy as np
import pandas as pd
```

## Create Data With One Class Label


```python
# Create NumPy array
x = np.array([['Texas'], 
              ['California'], 
              ['Texas'], 
              ['Delaware'], 
              ['Texas']])
```

## One-hot Encode Data (Method 1)


```python
# Create LabelBinzarizer object
one_hot = LabelBinarizer()

# One-hot encode data
one_hot.fit_transform(x)
```




    array([[0, 0, 1],
           [1, 0, 0],
           [0, 0, 1],
           [0, 1, 0],
           [0, 0, 1]])



## View Column Headers


```python
# View classes
one_hot.classes_
```




    array(['California', 'Delaware', 'Texas'],
          dtype='<U10')



## One-hot Encode Data (Method 2)


```python
# Dummy feature
pd.get_dummies(x[:,0])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>California</th>
      <th>Delaware</th>
      <th>Texas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>


