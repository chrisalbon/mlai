Title: Parallel Processing  
Slug: parallel_processing  
Summary: Lightweight Parallel Processing in Python.    
Date: 2016-01-23 12:00  
Category: Python  
Tags: Basics    
Authors: Chris Albon  

This tutorial is inspired by Chris Kiehl's [great post on multiprocessing](http://chriskiehl.com/article/parallelism-in-one-line/).

## Preliminaries


```python
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 
```

## Create Some Data


```python
# Create a list of some data
data = range(29999)
```

## Create An Operation To Execute On The Data


```python
# Create a function that takes a data point
def some_function(datum):
    # and returns the datum raised to the power of itself
    return datum**datum
```

## Traditional Approach


```python
%%time

# Create an empty for the results
results = [] 

# For each value in the data
for datum in data:
    # Append the output of the function when applied to that datum
    results.append(some_function(datum))
```

    CPU times: user 2min 2s, sys: 1.7 s, total: 2min 4s
    Wall time: 2min 8s


## Parallelism Approach


```python
# Create a pool of workers equaling cores on the machine
pool = ThreadPool() 
```


```python
%%time

# Apply (map) some_function to the data using the pool of workers
results = pool.map(some_function, data)

# Close the pool
pool.close() 

# Combine the results of the workers
pool.join() 
```

    CPU times: user 1min 56s, sys: 1.59 s, total: 1min 57s
    Wall time: 1min 57s

