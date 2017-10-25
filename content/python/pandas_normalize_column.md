Title: Normalize A Column In Pandas  
Slug: pandas_normalize_column  
Summary: Normalize A Column In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

Based on: [Sandman via StackOverflow](http://stackoverflow.com/questions/26414913/normalize-rows-of-pandas-data-frame).

## Preliminaries


```python
# Import required modules
import pandas as pd
from sklearn import preprocessing

# Set charts to view inline
%matplotlib inline
```

## Create Unnormalized Data


```python
# Create an example dataframe with a column of unnormalized data
data = {'score': [234,24,14,27,-74,46,73,-18,59,160]}
df = pd.DataFrame(data)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>234</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-74</td>
    </tr>
    <tr>
      <th>5</th>
      <td>46</td>
    </tr>
    <tr>
      <th>6</th>
      <td>73</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-18</td>
    </tr>
    <tr>
      <th>8</th>
      <td>59</td>
    </tr>
    <tr>
      <th>9</th>
      <td>160</td>
    </tr>
  </tbody>
</table>
</div>




```python
# View the unnormalized data
df['score'].plot(kind='bar')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x113a84eb8>




![png](pandas_normalize_column_files/pandas_normalize_column_5_1.png)


## Normalize The Column


```python
# Create x, where x the 'scores' column's values as floats
x = df['score'].values.astype(float)

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(x)

# Run the normalizer on the dataframe
df_normalized = pd.DataFrame(x_scaled)
```

    /Users/chrisralbon/anaconda/lib/python3.5/site-packages/sklearn/preprocessing/data.py:324: DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and will raise ValueError in 0.19. Reshape your data either using X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.
      warnings.warn(DEPRECATION_MSG_1D, DeprecationWarning)
    /Users/chrisralbon/anaconda/lib/python3.5/site-packages/sklearn/preprocessing/data.py:359: DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and will raise ValueError in 0.19. Reshape your data either using X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.
      warnings.warn(DEPRECATION_MSG_1D, DeprecationWarning)



```python
# View the dataframe
df_normalized
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.318182</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.285714</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.327922</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.389610</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.477273</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.181818</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.431818</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.759740</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plot the dataframe
df_normalized.plot(kind='bar')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x115f11278>




![png](pandas_normalize_column_files/pandas_normalize_column_9_1.png)

