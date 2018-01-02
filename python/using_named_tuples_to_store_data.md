Title: Using Named Tuples To Store Data  
Slug: using_named_tuples_to_store_data  
Summary: Using Named Tuples To Store Data in Python.    
Date: 2016-01-23 12:00  
Category: Python  
Tags: Basics    
Authors: Chris Albon  

Interesting in learning more? Check out [Fluent Python](http://amzn.to/2jYU506)

## Preliminaries


```python
from collections import namedtuple
```

## Create A Named Tuple


```python
Vehicle = namedtuple('Vehicle', 'make model wheels manual')
```

## Create An Entry


```python
forrester = Vehicle('Forrester', 'Subaru', 4, True)
```

## View The Data In Entry


```python
forrester.model
```




    'Subaru'




```python
forrester.wheels
```




    4


