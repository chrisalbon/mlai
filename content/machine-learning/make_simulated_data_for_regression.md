Title: Make Simulated Data For Regression  
Slug: make_simulated_data_for_regression  
Summary: Make a simulated dataset for regression using scikit-learn.  
Date: 2017-01-16 12:00  
Category: Machine Learning  
Tags: Basics  
Authors: Chris Albon   

## Preliminaries


```python
import pandas as pd
from sklearn.datasets import make_regression
```

## Create Simulated Data


```python
# Generate fetures, outputs, and true coefficient of 100 samples,
features, output, coef = make_regression(n_samples = 100,
                                         # three features
                                         n_features = 3,
                                         # where only two features are useful,
                                         n_informative = 2,
                                         # a single target value per observation
                                         n_targets = 1,
                                         # 0.0 standard deviation of the guassian noise
                                         noise = 0.0,
                                         # show the true coefficient used to generated the data
                                         coef = True)
```

## View Simulated Data


```python
# View the features of the first five rows
pd.DataFrame(features, columns=['Store 1', 'Store 2', 'Store 3']).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Store 1</th>
      <th>Store 2</th>
      <th>Store 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.166697</td>
      <td>-0.177142</td>
      <td>-2.329568</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.093566</td>
      <td>-0.544292</td>
      <td>0.685165</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.625958</td>
      <td>-0.193049</td>
      <td>1.168012</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.843925</td>
      <td>-0.567444</td>
      <td>-0.193631</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.079227</td>
      <td>-0.819236</td>
      <td>1.609171</td>
    </tr>
  </tbody>
</table>
</div>




```python
# View the output of the first five rows
pd.DataFrame(output, columns=['Sales']).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-149.387162</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-4.164344</td>
    </tr>
    <tr>
      <th>2</th>
      <td>52.166904</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-56.996180</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.246575</td>
    </tr>
  </tbody>
</table>
</div>




```python
# View the actual, true coefficients used to generate the data
pd.DataFrame(coef, columns=['True Coefficient Values'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>True Coefficient Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>80.654346</td>
    </tr>
    <tr>
      <th>2</th>
      <td>57.993548</td>
    </tr>
  </tbody>
</table>
</div>


