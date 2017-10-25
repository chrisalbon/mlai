Title: Make Simulated Data For Classification  
Slug: make_simulated_data_for_classification  
Summary: Make a simulated dataset for classification using scikit-learn.  
Date: 2017-01-16 12:00  
Category: Machine Learning  
Tags: Basics  
Authors: Chris Albon   

## Preliminaries


```python
from sklearn.datasets import make_classification
import pandas as pd
```

## Create Simulated Data


```python
# Create a simulated feature matrix and output vector with 100 samples,
features, output = make_classification(n_samples = 100,
                                       # ten features
                                       n_features = 10,
                                       # five features that actually predict the output's classes
                                       n_informative = 5,
                                       # five features that are random and unrelated to the output's classes
                                       n_redundant = 5,
                                       # three output classes
                                       n_classes = 3,
                                       # with 20% of observations in the first class, 30% in the second class,
                                       # and 50% in the third class. ('None' makes balanced classes)
                                       weights = [.2, .3, .8])
```

## View Data


```python
# View the first five observations and their 10 features
pd.DataFrame(features).head()
```




<div>
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
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.338796</td>
      <td>2.218025</td>
      <td>3.333541</td>
      <td>2.586772</td>
      <td>-2.050240</td>
      <td>-5.289060</td>
      <td>4.364050</td>
      <td>3.010074</td>
      <td>3.073564</td>
      <td>0.827317</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.535519</td>
      <td>1.964163</td>
      <td>-0.053789</td>
      <td>0.610150</td>
      <td>-4.256450</td>
      <td>-6.044707</td>
      <td>7.617702</td>
      <td>4.654903</td>
      <td>0.632368</td>
      <td>3.234648</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.249576</td>
      <td>-4.051890</td>
      <td>-4.578764</td>
      <td>-1.629710</td>
      <td>2.188123</td>
      <td>1.488968</td>
      <td>-1.977744</td>
      <td>-2.888737</td>
      <td>-4.957220</td>
      <td>3.599833</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.778789</td>
      <td>-4.797895</td>
      <td>-1.187821</td>
      <td>0.724315</td>
      <td>1.083952</td>
      <td>0.165924</td>
      <td>-0.352818</td>
      <td>0.615942</td>
      <td>-4.392519</td>
      <td>1.683278</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.856266</td>
      <td>0.568888</td>
      <td>-0.520666</td>
      <td>-1.970701</td>
      <td>0.597743</td>
      <td>2.224923</td>
      <td>0.065515</td>
      <td>0.250906</td>
      <td>-1.512495</td>
      <td>-0.859869</td>
    </tr>
  </tbody>
</table>
</div>




```python
# View the first five observation's classes
pd.DataFrame(output).head()
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
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>


