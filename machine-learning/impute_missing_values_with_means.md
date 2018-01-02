Title: Impute Missing Values With Means   
Slug: impute_missing_values_with_means   
Summary: Impute Missing Values With Means.   
Date: 2016-11-28 12:00    
Category: Machine Learning   
Tags: Preprocessing Structured Data  
Authors: Chris Albon

Mean imputation replaces missing values with the mean value of that feature/variable. Mean imputation is one of the most 'naive' imputation methods because unlike more complex methods like k-nearest neighbors imputation, it does not use the information we have about an observation to estimate a value for it.

## Preliminaries


```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
```

## Create Data


```python
# Create an empty dataset
df = pd.DataFrame()

# Create two variables called x0 and x1. Make the first value of x1 a missing value
df['x0'] = [0.3051,0.4949,0.6974,0.3769,0.2231,0.341,0.4436,0.5897,0.6308,0.5]
df['x1'] = [np.nan,0.2654,0.2615,0.5846,0.4615,0.8308,0.4962,0.3269,0.5346,0.6731]

# View the dataset
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x0</th>
      <th>x1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.3051</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.4949</td>
      <td>0.2654</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.6974</td>
      <td>0.2615</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.3769</td>
      <td>0.5846</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.2231</td>
      <td>0.4615</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.3410</td>
      <td>0.8308</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.4436</td>
      <td>0.4962</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.5897</td>
      <td>0.3269</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.6308</td>
      <td>0.5346</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.5000</td>
      <td>0.6731</td>
    </tr>
  </tbody>
</table>
</div>



## Fit Imputer


```python
# Create an imputer object that looks for 'Nan' values, then replaces them with the mean value of the feature by columns (axis=0)
mean_imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

# Train the imputor on the df dataset
mean_imputer = mean_imputer.fit(df)
```

## Apply Imputer


```python
# Apply the imputer to the df dataset
imputed_df = mean_imputer.transform(df.values)
```

## View Data


```python
# View the data
imputed_df
```




    array([[ 0.3051    ,  0.49273333],
           [ 0.4949    ,  0.2654    ],
           [ 0.6974    ,  0.2615    ],
           [ 0.3769    ,  0.5846    ],
           [ 0.2231    ,  0.4615    ],
           [ 0.341     ,  0.8308    ],
           [ 0.4436    ,  0.4962    ],
           [ 0.5897    ,  0.3269    ],
           [ 0.6308    ,  0.5346    ],
           [ 0.5       ,  0.6731    ]])



Notice that `0.49273333` is the imputed value, replacing the `np.NaN` value.
