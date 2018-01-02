Title: T-Tests  
Slug: t-tests  
Summary: T-tests in Python.    
Date: 2016-02-08 12:00  
Category: Statistics  
Tags: Basics
Authors: Chris Albon  

## Preliminaries


```python
from scipy import stats
import numpy as np
```

## Create Data


```python
# Create a list of 20 observations drawn from a random distribution 
# with mean 1 and a standard deviation of 1.5
x = np.random.normal(1, 1.5, 20)

# Create a list of 20 observations drawn from a random distribution 
# with mean 0 and a standard deviation of 1.5
y = np.random.normal(0, 1.5, 20)
```

## One Sample Two-Sided T-Test

Imagine the one sample T-test and drawing a (normally shaped) hill centered at `1` and "spread" out with a standard deviation of `1.5`, then placing a flag at `0` and looking at where on the hill the flag is location. Is it near the top? Far away from the hill? If the flag is near the very bottom of the hill or farther, then the t-test p-score will be below `0.05`.


```python
# Run a t-test to test if the mean of x is statistically significantly different than 0
pvalue = stats.ttest_1samp(x, 0)[1]

# View the p-value
pvalue
```




    0.00010976647757800537



## Two Variable Unpaired Two-Sided T-Test With Equal Variances

Imagine the one sample T-test and drawing two (normally shaped) hills centered at their means and their 'flattness' (individual spread) based on the standard deviation. The T-test looks at how much the two hills are overlapping. Are they basically on top of each other? Do just the bottoms of the hill just barely touch? If the tails of the hills are just barely overlapping or are not overlapping at all, the t-test p-score will be below 0.05.


```python
stats.ttest_ind(x, y)[1]
```




    0.00035082056802728071



## Two Variable Unpaired Two-Sided T-Test With Unequal Variances


```python
stats.ttest_ind(x, y, equal_var=False)[1]
```




    0.00035089238660076095



## Two Variable Paired Two-Sided T-Test

Paired T-tests are used when we are taking repeated samples and want to take into account the fact that the two distributions we are testing are paired.


```python
stats.ttest_rel(x, y)[1]
```




    0.00034222792790150386


