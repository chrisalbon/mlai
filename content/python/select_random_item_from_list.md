Title: Select Random Item From A Lists
Slug: select_random_item_from_list  
Summary: Select Random Item From A Lists in Python. 
Date: 2016-01-23 12:00  
Category: Python  
Tags: Basics    
Authors: Chris Albon  

Interesting in learning more? Check out [Fluent Python](http://amzn.to/2jYU506)

## Preliminaries


```python
from random import choice
```

## Create List


```python
# Make a list of crew members
crew_members = ['Steve', 'Stacy', 'Miller', 'Chris', 'Bill', 'Jack']
```

## Select Random Item From List


```python
# Choose a random crew member
choice(crew_members)
```




    'Stacy'


