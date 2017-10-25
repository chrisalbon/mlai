Title: Loading A CSV Into Pandas  
Slug: pandas_dataframe_importing_csv  
Summary: Loading A CSV Into Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### import modules


```python
import pandas as pd
import numpy as np
```

### Create dataframe (that we will be importing)


```python
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df
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
      <td>25,000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94,000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>.</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Save dataframe as csv in the working director


```python
df.to_csv('pandas_dataframe_importing_csv/example.csv')
```

### Load a csv


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv')
df
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
      <th>Unnamed: 0</th>
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
      <td>0</td>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25,000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94,000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Tina</td>
      <td>.</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Load a csv with no headers


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', header=None)
df
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>first_name</td>
      <td>last_name</td>
      <td>age</td>
      <td>preTestScore</td>
      <td>postTestScore</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25,000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94,000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>Tina</td>
      <td>.</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.0</td>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.0</td>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Load a csv while specifying column names


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
df
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
      <th>UID</th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Age</th>
      <th>Pre-Test Score</th>
      <th>Post-Test Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>first_name</td>
      <td>last_name</td>
      <td>age</td>
      <td>preTestScore</td>
      <td>postTestScore</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25,000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94,000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>Tina</td>
      <td>.</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.0</td>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.0</td>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Load a csv with setting the index column to UID


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', index_col='UID', names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
df
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
      <th>First Name</th>
      <th>Last Name</th>
      <th>Age</th>
      <th>Pre-Test Score</th>
      <th>Post-Test Score</th>
    </tr>
    <tr>
      <th>UID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>NaN</th>
      <td>first_name</td>
      <td>last_name</td>
      <td>age</td>
      <td>preTestScore</td>
      <td>postTestScore</td>
    </tr>
    <tr>
      <th>0.0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25,000</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94,000</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>Tina</td>
      <td>.</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Load a csv while setting the index columns to First Name and Last Name


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', index_col=['First Name', 'Last Name'], names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
df
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
      <th></th>
      <th>UID</th>
      <th>Age</th>
      <th>Pre-Test Score</th>
      <th>Post-Test Score</th>
    </tr>
    <tr>
      <th>First Name</th>
      <th>Last Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first_name</th>
      <th>last_name</th>
      <td>NaN</td>
      <td>age</td>
      <td>preTestScore</td>
      <td>postTestScore</td>
    </tr>
    <tr>
      <th>Jason</th>
      <th>Miller</th>
      <td>0.0</td>
      <td>42</td>
      <td>4</td>
      <td>25,000</td>
    </tr>
    <tr>
      <th>Molly</th>
      <th>Jacobson</th>
      <td>1.0</td>
      <td>52</td>
      <td>24</td>
      <td>94,000</td>
    </tr>
    <tr>
      <th>Tina</th>
      <th>.</th>
      <td>2.0</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>Jake</th>
      <th>Milner</th>
      <td>3.0</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>Amy</th>
      <th>Cooze</th>
      <td>4.0</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>





### Load a csv while specifying "." as missing values


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', na_values=['.'])
pd.isnull(df)
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
      <th>Unnamed: 0</th>
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
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



### Load a csv while specifying "." and "NA" as missing values in the Last Name column and "." as missing values in Pre-Test Score column


```python
sentinels = {'Last Name': ['.', 'NA'], 'Pre-Test Score': ['.']}
```


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', na_values=sentinels)
df
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
      <th>Unnamed: 0</th>
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
      <td>0</td>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25,000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94,000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Tina</td>
      <td>.</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Load a csv while skipping the top 3 rows


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', na_values=sentinels, skiprows=3)
df
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
      <th>2</th>
      <th>Tina</th>
      <th>.</th>
      <th>36</th>
      <th>31</th>
      <th>57</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Load a csv while interpreting "," in strings around numbers as thousands seperators


```python
df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', thousands=',')
df
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
      <th>Unnamed: 0</th>
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
      <td>0</td>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Tina</td>
      <td>.</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>.</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>.</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>


