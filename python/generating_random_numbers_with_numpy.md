Title: Generating Random Numbers With Numpy  
Slug: generating_random_numbers_with_numpy  
Summary: Generating Random Numbers With Numpy  
Date: 2016-05-01 12:00   
Category: Python  
Tags: Basics  
Authors: Chris Albon  

### Import Numpy


```python
import numpy as np
```

### Generate A Random Number From The Normal Distribution


```python
np.random.normal()
```




    0.5661104974399703



### Generate Four Random Numbers From The Normal Distribution


```python
np.random.normal(size=4)
```




    array([-1.03175853,  1.2867365 , -0.23560103, -1.05225393])



### Generate Four Random Numbers From The Uniform Distribution


```python
np.random.uniform(size=4)
```




    array([ 0.00193123,  0.51932356,  0.87656884,  0.33684494])



### Generate Four Random Integers Between 1 and 100


```python
np.random.randint(low=1, high=100, size=4)
```




    array([96, 25, 94, 77])


