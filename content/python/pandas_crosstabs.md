Title: Crosstabs In Pandas  
Slug: pandas_crosstabs  
Summary: Crosstabs In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### Import pandas


```python
import pandas as pd
```


```python
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['infantry', 'infantry', 'cavalry', 'cavalry', 'infantry', 'infantry', 'cavalry', 'cavalry','infantry', 'infantry', 'cavalry', 'cavalry'], 
        'experience': ['veteran', 'rookie', 'veteran', 'rookie', 'veteran', 'rookie', 'veteran', 'rookie','veteran', 'rookie', 'veteran', 'rookie'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'experience', 'name', 'preTestScore', 'postTestScore'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>experience</th>
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nighthawks</td>
      <td>infantry</td>
      <td>veteran</td>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nighthawks</td>
      <td>infantry</td>
      <td>rookie</td>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nighthawks</td>
      <td>cavalry</td>
      <td>veteran</td>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nighthawks</td>
      <td>cavalry</td>
      <td>rookie</td>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragoons</td>
      <td>infantry</td>
      <td>veteran</td>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragoons</td>
      <td>infantry</td>
      <td>rookie</td>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragoons</td>
      <td>cavalry</td>
      <td>veteran</td>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragoons</td>
      <td>cavalry</td>
      <td>rookie</td>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Scouts</td>
      <td>infantry</td>
      <td>veteran</td>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Scouts</td>
      <td>infantry</td>
      <td>rookie</td>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Scouts</td>
      <td>cavalry</td>
      <td>veteran</td>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Scouts</td>
      <td>cavalry</td>
      <td>rookie</td>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Create a crosstab table by company and regiment

Counting the number of observations by regiment and category


```python
pd.crosstab(df.regiment, df.company, margins=True)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>company</th>
      <th>cavalry</th>
      <th>infantry</th>
      <th>All</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dragoons</th>
      <td>2</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Nighthawks</th>
      <td>2</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Scouts</th>
      <td>2</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>All</th>
      <td>6</td>
      <td>6</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



### Create a crosstab of the number of rookie and veteran cavalry and infantry soldiers per regiment


```python
pd.crosstab([df.company, df.experience], df.regiment,  margins=True)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>Dragoons</th>
      <th>Nighthawks</th>
      <th>Scouts</th>
      <th>All</th>
    </tr>
    <tr>
      <th>company</th>
      <th>experience</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">cavalry</th>
      <th>rookie</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>veteran</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">infantry</th>
      <th>rookie</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>veteran</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>All</th>
      <th></th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>


