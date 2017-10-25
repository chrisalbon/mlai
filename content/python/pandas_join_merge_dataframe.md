Title: Join And Merge Pandas Dataframe  
Slug: pandas_join_merge_dataframe  
Summary: Join And Merge Pandas Dataframe  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### import modules


```python
import pandas as pd
from IPython.display import display
from IPython.display import Image
```

### Create a dataframe


```python
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_a
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
    </tr>
  </tbody>
</table>
</div>



### Create a second dataframe


```python
raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_b
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>Bran</td>
      <td>Balwner</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>Bryce</td>
      <td>Brice</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>Betty</td>
      <td>Btisan</td>
    </tr>
  </tbody>
</table>
</div>



### Create a third dataframe


```python
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data, columns = ['subject_id','test_id'])
df_n
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>test_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>51</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>61</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>16</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>14</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>15</td>
    </tr>
    <tr>
      <th>7</th>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>10</td>
      <td>61</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



### Join the two dataframes along rows


```python
df_new = pd.concat([df_a, df_b])
df_new
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
    </tr>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>Bran</td>
      <td>Balwner</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>Bryce</td>
      <td>Brice</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>Betty</td>
      <td>Btisan</td>
    </tr>
  </tbody>
</table>
</div>



### Join the two dataframes along columns


```python
pd.concat([df_a, df_b], axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>subject_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
      <td>4</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
      <td>5</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
      <td>6</td>
      <td>Bran</td>
      <td>Balwner</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>7</td>
      <td>Bryce</td>
      <td>Brice</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>8</td>
      <td>Betty</td>
      <td>Btisan</td>
    </tr>
  </tbody>
</table>
</div>



### Merge two dataframes along the subject_id value


```python
pd.merge(df_new, df_n, on='subject_id')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>test_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
      <td>51</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>61</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Billy</td>
      <td>Bonder</td>
      <td>61</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>16</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5</td>
      <td>Brian</td>
      <td>Black</td>
      <td>16</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Bryce</td>
      <td>Brice</td>
      <td>14</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Betty</td>
      <td>Btisan</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### Merge two dataframes with both the left and right dataframes using the subject_id key


```python
pd.merge(df_new, df_n, left_on='subject_id', right_on='subject_id')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>test_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
      <td>51</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>61</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Billy</td>
      <td>Bonder</td>
      <td>61</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>16</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5</td>
      <td>Brian</td>
      <td>Black</td>
      <td>16</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Bryce</td>
      <td>Brice</td>
      <td>14</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Betty</td>
      <td>Btisan</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### Merge with outer join

"Full outer join produces the set of all records in Table A and Table B, with matching records from both sides where available. If there is no match, the missing side will contain null." - [source](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)


```python
pd.merge(df_a, df_b, on='subject_id', how='outer')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name_x</th>
      <th>last_name_x</th>
      <th>first_name_y</th>
      <th>last_name_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Bran</td>
      <td>Balwner</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Bryce</td>
      <td>Brice</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Betty</td>
      <td>Btisan</td>
    </tr>
  </tbody>
</table>
</div>



### Merge with inner join

"Inner join produces only the set of records that match in both Table A and Table B." - [source](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)


```python
pd.merge(df_a, df_b, on='subject_id', how='inner')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name_x</th>
      <th>last_name_x</th>
      <th>first_name_y</th>
      <th>last_name_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
  </tbody>
</table>
</div>



### Merge with right join


```python
pd.merge(df_a, df_b, on='subject_id', how='right')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name_x</th>
      <th>last_name_x</th>
      <th>first_name_y</th>
      <th>last_name_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Bran</td>
      <td>Balwner</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Bryce</td>
      <td>Brice</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Betty</td>
      <td>Btisan</td>
    </tr>
  </tbody>
</table>
</div>



### Merge with left join

"Left outer join produces a complete set of records from Table A, with the matching records (where available) in Table B. If there is no match, the right side will contain null." - [source](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)


```python
pd.merge(df_a, df_b, on='subject_id', how='left')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name_x</th>
      <th>last_name_x</th>
      <th>first_name_y</th>
      <th>last_name_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
  </tbody>
</table>
</div>



### Merge while adding a suffix to duplicate column names


```python
pd.merge(df_a, df_b, on='subject_id', how='left', suffixes=('_left', '_right'))
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id</th>
      <th>first_name_left</th>
      <th>last_name_left</th>
      <th>first_name_right</th>
      <th>last_name_right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
  </tbody>
</table>
</div>



### Merge based on indexes


```python
pd.merge(df_a, df_b, right_index=True, left_index=True)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject_id_x</th>
      <th>first_name_x</th>
      <th>last_name_x</th>
      <th>subject_id_y</th>
      <th>first_name_y</th>
      <th>last_name_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alex</td>
      <td>Anderson</td>
      <td>4</td>
      <td>Billy</td>
      <td>Bonder</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Amy</td>
      <td>Ackerman</td>
      <td>5</td>
      <td>Brian</td>
      <td>Black</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Allen</td>
      <td>Ali</td>
      <td>6</td>
      <td>Bran</td>
      <td>Balwner</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alice</td>
      <td>Aoni</td>
      <td>7</td>
      <td>Bryce</td>
      <td>Brice</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Ayoung</td>
      <td>Atiches</td>
      <td>8</td>
      <td>Betty</td>
      <td>Btisan</td>
    </tr>
  </tbody>
</table>
</div>


