Title: Expand Cells Containing Lists Into Their Own Variables In Pandas  
Slug: pandas_expand_cells_containing_lists  
Summary: Expand Cells Containing Lists Into Their Own Variables In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# import pandas
import pandas as pd
```


```python
# create a dataset
raw_data = {'score': [1,2,3], 
        'tags': [['apple','pear','guava'],['truck','car','plane'],['cat','dog','mouse']]}
df = pd.DataFrame(raw_data, columns = ['score', 'tags'])

# view the dataset
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
      <th>tags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>[apple, pear, guava]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>[truck, car, plane]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>[cat, dog, mouse]</td>
    </tr>
  </tbody>
</table>
</div>




```python
# expand df.tags into its own dataframe
tags = df['tags'].apply(pd.Series)

# rename each variable is tags
tags = tags.rename(columns = lambda x : 'tag_' + str(x))

# view the tags dataframe
tags
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tag_0</th>
      <th>tag_1</th>
      <th>tag_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apple</td>
      <td>pear</td>
      <td>guava</td>
    </tr>
    <tr>
      <th>1</th>
      <td>truck</td>
      <td>car</td>
      <td>plane</td>
    </tr>
    <tr>
      <th>2</th>
      <td>cat</td>
      <td>dog</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>




```python
# join the tags dataframe back to the original dataframe
pd.concat([df[:], tags[:]], axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
      <th>tags</th>
      <th>tag_0</th>
      <th>tag_1</th>
      <th>tag_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>[apple, pear, guava]</td>
      <td>apple</td>
      <td>pear</td>
      <td>guava</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>[truck, car, plane]</td>
      <td>truck</td>
      <td>car</td>
      <td>plane</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>[cat, dog, mouse]</td>
      <td>cat</td>
      <td>dog</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>


