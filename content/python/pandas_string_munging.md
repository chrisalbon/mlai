Title: String Munging In Dataframe  
Slug: pandas_string_munging  
Summary: String Munging In Dataframe  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### import modules


```python
import pandas as pd
import numpy as np
import re as re
```

### Create dataframe


```python
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'email': ['jas203@gmail.com', 'momomolly@gmail.com', np.NAN, 'battler@milner.com', 'Ames1234@yahoo.com'], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'email', 'preTestScore', 'postTestScore'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>email</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>jas203@gmail.com</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>momomolly@gmail.com</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>NaN</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>battler@milner.com</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>Ames1234@yahoo.com</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Which strings in the email column contains 'gmail'


```python
df['email'].str.contains('gmail')
```




    0     True
    1     True
    2      NaN
    3    False
    4    False
    Name: email, dtype: object



### Create a regular expression pattern that breaks apart emails


```python
pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'
```

### Find everything in df.email that contains that pattern


```python
df['email'].str.findall(pattern, flags=re.IGNORECASE)
```




    0       [(jas203, gmail, com)]
    1    [(momomolly, gmail, com)]
    2                          NaN
    3     [(battler, milner, com)]
    4     [(Ames1234, yahoo, com)]
    Name: email, dtype: object



### Create a pandas series containing the email elements


```python
matches = df['email'].str.match(pattern, flags=re.IGNORECASE)
matches
```

    /Users/chrisralbon/anaconda/lib/python3.5/site-packages/ipykernel/__main__.py:1: FutureWarning: In future versions of pandas, match will change to always return a bool indexer.
      if __name__ == '__main__':





    0       (jas203, gmail, com)
    1    (momomolly, gmail, com)
    2                        NaN
    3     (battler, milner, com)
    4     (Ames1234, yahoo, com)
    Name: email, dtype: object



### Select the domains of the df.email


```python
matches.str[1]
```




    0     gmail
    1     gmail
    2       NaN
    3    milner
    4     yahoo
    Name: email, dtype: object


