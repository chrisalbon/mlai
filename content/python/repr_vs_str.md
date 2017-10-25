Title: repr vs. str  
Slug: repr_vs_str  
Summary: repr vs. str in Python.    
Date: 2016-01-23 12:00  
Category: Python  
Tags: Basics    
Authors: Chris Albon  

Interesting in learning more? Check out [Fluent Python](http://amzn.to/2jYU506)

## Preliminaries


```python
import datetime
```

## Create A Simple Object


```python
class Regiment(object):

    def __init__(self, date=datetime.datetime.now()):
        self.date = date

    def __repr__(self):
        return date

    def __str__(self):
        return str(date)
```

`__repr__` is for the developer. It is string representation of the object and the code needed to reproduce the object. 

`__str__` is the output for the end user. It prints what the user wants to see.
