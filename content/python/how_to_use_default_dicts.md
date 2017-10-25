Title: How To Use Default Dicts  
Slug: how_to_use_default_dicts  
Summary: How To Use Default Dicts in Python.    
Date: 2016-01-23 12:00  
Category: Python  
Tags: Basics    
Authors: Chris Albon  

Interesting in learning more? Check out [Fluent Python](http://amzn.to/2jYU506)

## Preliminaries


```python
import collections
```

## Create A DefaultDict

Default Dicts work just like regular dictionaries, except a key is called that doesn't have a value, a default value (note: value, not key) is supplied.


```python
# Create a defaultdict with the default value of 0 (int's default value is 0)
arrests = collections.defaultdict(int) 
```

## Add A New Key With A Value


```python
# Add an entry of a person with 10 arrests
arrests['Sarah Miller'] = 10
```


```python
# View dictionary
arrests
```




    defaultdict(int, {'Sarah Miller': 10})



## Add A New Key Without A Value


```python
# Add an entry of a person with no value for arrests,
# thus the default value is used
arrests['Bill James']
```




    0




```python
# View dictionary
arrests
```




    defaultdict(int, {'Bill James': 0, 'Sarah Miller': 10})


