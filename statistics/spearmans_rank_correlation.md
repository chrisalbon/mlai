Title: Spearman's Rank Correlation  
Slug: spearmans_rank_correlation  
Summary: Spearman's Rank Correlation in Python.    
Date: 2016-02-08 12:00  
Category: Statistics  
Tags: Basics
Authors: Chris Albon  

## Preliminaries


```python
import numpy as np
import pandas as pd
import scipy.stats
```

## Create Data


```python
# Create two lists of random values
x = [1,2,3,4,5,6,7,8,9]
y = [2,1,2,4.5,7,6.5,6,9,9.5]
```

## Calculate Spearman's Rank Correlation

Spearman's rank correlation is the Pearson's correlation coefficient of the ranked version of the variables.


```python
# Create a function that takes in x's and y's
def spearmans_rank_correlation(xs, ys):
    
    # Calculate the rank of x's
    xranks = pd.Series(xs).rank()
    
    # Caclulate the ranking of the y's
    yranks = pd.Series(ys).rank()
    
    # Calculate Pearson's correlation coefficient on the ranked versions of the data
    return scipy.stats.pearsonr(xranks, yranks)
```


```python
# Run the function
spearmans_rank_correlation(x, y)[0]
```




    0.90377360145618091



## Calculate Spearman's Correlation Using SciPy


```python
# Just to check our results, here it Spearman's using Scipy
scipy.stats.spearmanr(x, y)[0]
```




    0.90377360145618102


