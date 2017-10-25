Title: Simple Example Dataframes In Pandas  
Slug: pandas_dataframe_examples  
Summary: Simple Example Dataframes In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### import modules


```python
import pandas as pd
```

### Create dataframe


```python
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
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
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Create 2nd dataframe


```python
raw_data_2 = {'first_name': ['Sarah', 'Gueniva', 'Know', 'Sara', 'Cat'], 
        'last_name': ['Mornig', 'Jaker', 'Alom', 'Ormon', 'Koozer'], 
        'age': [53, 26, 72, 73, 24], 
        'preTestScore': [13, 52, 72, 26, 26],
        'postTestScore': [82, 52, 56, 234, 254]}
df_2 = pd.DataFrame(raw_data_2, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df_2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarah</td>
      <td>Mornig</td>
      <td>53</td>
      <td>13</td>
      <td>82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gueniva</td>
      <td>Jaker</td>
      <td>26</td>
      <td>52</td>
      <td>52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Know</td>
      <td>Alom</td>
      <td>72</td>
      <td>72</td>
      <td>56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sara</td>
      <td>Ormon</td>
      <td>73</td>
      <td>26</td>
      <td>234</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cat</td>
      <td>Koozer</td>
      <td>24</td>
      <td>26</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>



### Create 3rd dataframe


```python
raw_data_3 = {'first_name': ['Sarah', 'Gueniva', 'Know', 'Sara', 'Cat'], 
        'last_name': ['Mornig', 'Jaker', 'Alom', 'Ormon', 'Koozer'],
         'postTestScore_2': [82, 52, 56, 234, 254]}
df_3 = pd.DataFrame(raw_data_3, columns = ['first_name', 'last_name', 'postTestScore_2'])
df_3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>postTestScore_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarah</td>
      <td>Mornig</td>
      <td>82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gueniva</td>
      <td>Jaker</td>
      <td>52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Know</td>
      <td>Alom</td>
      <td>56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sara</td>
      <td>Ormon</td>
      <td>234</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cat</td>
      <td>Koozer</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>


