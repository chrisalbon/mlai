Title: Effect Of Alpha On Lasso Regression    
Slug: effect_of_alpha_on_lasso_regression   
Summary: The effect of alpha values on lasso regression in Scikit-Learn   
Date: 2016-11-01 12:00  
Category: Machine Learning  
Tags: Feature Selection  
Authors: Chris Albon  

Often we want conduct a process called [regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)), wherein we penalize the number of features in a model in order to only keep the most important features. This can be particularly important when you have a dataset with 100,000+ features.

[Lasso regression](https://en.wikipedia.org/wiki/Lasso_(statistics)) is a common modeling technique to do regularization. The math behind it is pretty interesting, but practically, what you need to know is that Lasso regression comes with a parameter, `alpha`, and the higher the `alpha`, the most feature coefficients are zero.

That is, when `alpha` is `0`, Lasso regression produces the same coefficients as a linear regression. When `alpha` is very very large, all coefficients are zero.

In this tutorial, I run three lasso regressions, with varying levels of alpha, and show the resulting effect on the coefficients.

## Preliminaries


```python
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston
import pandas as pd
```

## Load Data


```python
boston = load_boston()
scaler = StandardScaler()
X = scaler.fit_transform(boston["data"])
Y = boston["target"]
names = boston["feature_names"]
```

## Run Three Lasso Regressions, Varying Alpha Levels


```python
# Create a function called lasso,
def lasso(alphas):
    '''
    Takes in a list of alphas. Outputs a dataframe containing the coefficients of lasso regressions from each alpha.
    '''
    # Create an empty data frame
    df = pd.DataFrame()
    
    # Create a column of feature names
    df['Feature Name'] = names
    
    # For each alpha value in the list of alpha values,
    for alpha in alphas:
        # Create a lasso regression with that alpha value,
        lasso = Lasso(alpha=alpha)
        
        # Fit the lasso regression
        lasso.fit(X, Y)
        
        # Create a column name for that alpha value
        column_name = 'Alpha = %f' % alpha

        # Create a column of coefficient values
        df[column_name] = lasso.coef_
        
    # Return the datafram    
    return df
```


```python
# Run the function called, Lasso
lasso([.0001, .5, 10])
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
      <th>Feature Name</th>
      <th>Alpha = 0.000100</th>
      <th>Alpha = 0.500000</th>
      <th>Alpha = 10.000000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CRIM</td>
      <td>-0.920130</td>
      <td>-0.106977</td>
      <td>-0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ZN</td>
      <td>1.080498</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>INDUS</td>
      <td>0.142027</td>
      <td>-0.000000</td>
      <td>-0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CHAS</td>
      <td>0.682235</td>
      <td>0.397399</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NOX</td>
      <td>-2.059250</td>
      <td>-0.000000</td>
      <td>-0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>RM</td>
      <td>2.670814</td>
      <td>2.973323</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>AGE</td>
      <td>0.020680</td>
      <td>-0.000000</td>
      <td>-0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>DIS</td>
      <td>-3.104070</td>
      <td>-0.169378</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>RAD</td>
      <td>2.656950</td>
      <td>-0.000000</td>
      <td>-0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>TAX</td>
      <td>-2.074110</td>
      <td>-0.000000</td>
      <td>-0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PTRATIO</td>
      <td>-2.061921</td>
      <td>-1.599574</td>
      <td>-0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>B</td>
      <td>0.856553</td>
      <td>0.545715</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>LSTAT</td>
      <td>-3.748470</td>
      <td>-3.668884</td>
      <td>-0.0</td>
    </tr>
  </tbody>
</table>
</div>



Notice that as the alpha value increases, more features have a coefficient of 0.
