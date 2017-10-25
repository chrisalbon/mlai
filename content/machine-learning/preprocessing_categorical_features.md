Title: Preprocessing Categorical Features  
Slug: preprocessing_categorical_features  
Summary: Preprocessing Categorical Features  
Date: 2016-11-01 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon   

Often, machine learning methods (e.g. logistic regression, SVM with a linear kernel, etc) will require that categorical variables be converted into dummy variables (also called OneHot encoding). For example, a single feature `Fruit` would be converted into three features, `Apples`, `Oranges`, and `Bananas`, one for each category in the categorical feature.

There are common ways to preprocess categorical features: using pandas or scikit-learn.

## Preliminaries


```python
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
import pandas as pd
```

## Create Data


```python
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>San Francisco</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>Baltimore</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>Miami</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>Douglas</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>Boston</td>
    </tr>
  </tbody>
</table>
</div>



## Convert Nominal Categorical Feature Into Dummy Variables Using Pandas


```python
# Create dummy variables for every unique category in df.city
pd.get_dummies(df["city"])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Baltimore</th>
      <th>Boston</th>
      <th>Douglas</th>
      <th>Miami</th>
      <th>San Francisco</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## Convert Nominal Categorical Data Into Dummy (OneHot) Features Using Scikit


```python
# Convert strings categorical names to integers
integerized_data = preprocessing.LabelEncoder().fit_transform(df["city"])

# View data
integerized_data
```




    array([4, 0, 3, 2, 1])




```python
# Convert integer categorical representations to OneHot encodings
preprocessing.OneHotEncoder().fit_transform(integerized_data.reshape(-1,1)).toarray()
```




    array([[ 0.,  0.,  0.,  0.,  1.],
           [ 1.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  1.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  1.,  0.,  0.,  0.]])



Note that the output of pd.get_dummies() and the scikit methods produces the same output matrix.
