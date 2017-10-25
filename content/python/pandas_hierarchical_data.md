Title: Hierarchical Data In Pandas  
Slug: pandas_hierarchical_data  
Summary: Hierarchical Data In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# import modules
import pandas as pd
```


```python
# Create dataframe
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
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
      <th>regiment</th>
      <th>company</th>
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Set the hierarchical index but leave the columns inplace
df.set_index(['regiment', 'company'], drop=False)
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
      <th>regiment</th>
      <th>company</th>
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Set the hierarchical index to be by regiment, and then by company
df = df.set_index(['regiment', 'company'])
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
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th>company</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Nighthawks</th>
      <th>1st</th>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1st</th>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Dragoons</th>
      <th>1st</th>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>1st</th>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Scouts</th>
      <th>1st</th>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>1st</th>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# View the index
df.index
```




    MultiIndex(levels=[['Dragoons', 'Nighthawks', 'Scouts'], ['1st', '2nd']],
               labels=[[1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]],
               names=['regiment', 'company'])




```python
# Swap the levels in the index
df.swaplevel('regiment', 'company')
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
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
    <tr>
      <th>company</th>
      <th>regiment</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1st</th>
      <th>Nighthawks</th>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>Nighthawks</th>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2nd</th>
      <th>Nighthawks</th>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>Nighthawks</th>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1st</th>
      <th>Dragoons</th>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>Dragoons</th>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2nd</th>
      <th>Dragoons</th>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>Dragoons</th>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1st</th>
      <th>Scouts</th>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>Scouts</th>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2nd</th>
      <th>Scouts</th>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>Scouts</th>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Summarize the results by regiment
df.sum(level='regiment')
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
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dragoons</th>
      <td>62</td>
      <td>246</td>
    </tr>
    <tr>
      <th>Nighthawks</th>
      <td>61</td>
      <td>238</td>
    </tr>
    <tr>
      <th>Scouts</th>
      <td>10</td>
      <td>264</td>
    </tr>
  </tbody>
</table>
</div>


