Title: Using Seaborn To Visualize A Pandas Dataframe  
Slug: pandas_with_seaborn  
Summary: Using Seaborn To Visualize A Pandas Dataframe  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Preliminaries


```python
import pandas as pd
%matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
df = pd.DataFrame()

df['x'] = random.sample(range(1, 100), 25)
df['y'] = random.sample(range(1, 100), 25)
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>42</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2</th>
      <td>52</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14</td>
      <td>69</td>
    </tr>
  </tbody>
</table>
</div>



## Scatterplot


```python
sns.lmplot('x', 'y', data=df, fit_reg=False)
```




    <seaborn.axisgrid.FacetGrid at 0x114563b00>




![png](pandas_with_seaborn_files/pandas_with_seaborn_6_1.png)


## Density Plot


```python
sns.kdeplot(df.y)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x113ea2ef0>




![png](pandas_with_seaborn_files/pandas_with_seaborn_8_1.png)



```python
sns.kdeplot(df.y, df.x)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x113d7fef0>




![png](pandas_with_seaborn_files/pandas_with_seaborn_9_1.png)



```python
sns.distplot(df.x)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x114294160>




![png](pandas_with_seaborn_files/pandas_with_seaborn_10_1.png)


## Histogram


```python
plt.hist(df.x, alpha=.3)
sns.rugplot(df.x);
```


![png](pandas_with_seaborn_files/pandas_with_seaborn_12_0.png)


## Boxplot 


```python
sns.boxplot([df.y, df.x])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1142b8b38>




![png](pandas_with_seaborn_files/pandas_with_seaborn_14_1.png)


## Violin Plot


```python
sns.violinplot([df.y, df.x])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x114444a58>




![png](pandas_with_seaborn_files/pandas_with_seaborn_16_1.png)


## Heatmap


```python
sns.heatmap([df.y, df.x], annot=True, fmt="d")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x114530c88>




![png](pandas_with_seaborn_files/pandas_with_seaborn_18_1.png)


## Clustermap


```python
sns.clustermap(df)
```




    <seaborn.matrix.ClusterGrid at 0x116f313c8>




![png](pandas_with_seaborn_files/pandas_with_seaborn_20_1.png)

