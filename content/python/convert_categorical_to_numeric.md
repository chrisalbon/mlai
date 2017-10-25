Title: Convert A String Categorical Variable To A Numeric Variable
Slug: convert_categorical_to_numeric  
Summary: Convert A String Categorical Variable To A Numeric Variable 
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

Originally from: [Data Origami](https://dataorigami.net/).

### import modules


```python
import pandas as pd
```

### Create dataframe


```python
raw_data = {'patient': [1, 1, 1, 2, 2], 
        'obs': [1, 2, 3, 1, 2], 
        'treatment': [0, 1, 0, 1, 0],
        'score': ['strong', 'weak', 'normal', 'weak', 'strong']} 
df = pd.DataFrame(raw_data, columns = ['patient', 'obs', 'treatment', 'score'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>patient</th>
      <th>obs</th>
      <th>treatment</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>strong</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>weak</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>normal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>weak</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>strong</td>
    </tr>
  </tbody>
</table>
</div>



### Create a function that converts all values of df['score'] into numbers


```python
def score_to_numeric(x):
    if x=='strong':
        return 3
    if x=='normal':
        return 2
    if x=='weak':
        return 1
```

### Apply the function to the score variable


```python
df['score_num'] = df['score'].apply(score_to_numeric)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>patient</th>
      <th>obs</th>
      <th>treatment</th>
      <th>score</th>
      <th>score_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>strong</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>weak</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>normal</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>weak</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>strong</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>


