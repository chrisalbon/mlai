Title: Concurrent Processing  
Slug: concurrent_processing   
Summary: Concurrent Processing in Python.    
Date: 2016-01-23 12:00  
Category: Python  
Tags: Basics    
Authors: Chris Albon  

Interesting in learning more? Check out [Fluent Python](http://amzn.to/2jYU506)

## Preliminaries


```python
from concurrent import futures
```

## Create Data


```python
data = range(100)
```

## Create Function


```python
# Create some function that takes a value
def some_function(value):
    # And outputs it raised to its own power
    return value**value
```

## Run The Function On The Data Concurrently


```python
# With a pool of workers
with futures.ProcessPoolExecutor() as executor:
    # Map the function to the data
    result = executor.map(some_function, data)
```

## View Results


```python
# List the first 5 outputs
list(result)[0:5]
```




    [1, 1, 4, 27, 256]


