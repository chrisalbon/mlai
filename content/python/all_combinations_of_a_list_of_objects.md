Title: All Combinations For A List Of Objects  
Slug: all_combinations_of_a_list_of_objects  
Summary: All Combinations For A List Of Objects  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Preliminary


```python
# Import combinations with replacements from itertools
from itertools import combinations_with_replacement
```

## Create a list of objects


```python
# Create a list of objects to combine
list_of_objects = ['warplanes', 'armor', 'infantry']
```

## Find all combinations (with replacement) for the list


```python
# Create an empty list object to hold the results of the loop
combinations = []

# Create a loop for every item in the length of list_of_objects, that,
for i in list(range(len(list_of_objects))):
    # Finds every combination (with replacement) for each object in the list
    combinations.append(list(combinations_with_replacement(list_of_objects, i+1)))
    
# View the results
combinations
```




    [[('warplanes',), ('armor',), ('infantry',)],
     [('warplanes', 'warplanes'),
      ('warplanes', 'armor'),
      ('warplanes', 'infantry'),
      ('armor', 'armor'),
      ('armor', 'infantry'),
      ('infantry', 'infantry')],
     [('warplanes', 'warplanes', 'warplanes'),
      ('warplanes', 'warplanes', 'armor'),
      ('warplanes', 'warplanes', 'infantry'),
      ('warplanes', 'armor', 'armor'),
      ('warplanes', 'armor', 'infantry'),
      ('warplanes', 'infantry', 'infantry'),
      ('armor', 'armor', 'armor'),
      ('armor', 'armor', 'infantry'),
      ('armor', 'infantry', 'infantry'),
      ('infantry', 'infantry', 'infantry')]]




```python
# Flatten the list of lists into just a list
combinations = [i for row in combinations for i in row]

# View the results
combinations
```




    [('warplanes',),
     ('armor',),
     ('infantry',),
     ('warplanes', 'warplanes'),
     ('warplanes', 'armor'),
     ('warplanes', 'infantry'),
     ('armor', 'armor'),
     ('armor', 'infantry'),
     ('infantry', 'infantry'),
     ('warplanes', 'warplanes', 'warplanes'),
     ('warplanes', 'warplanes', 'armor'),
     ('warplanes', 'warplanes', 'infantry'),
     ('warplanes', 'armor', 'armor'),
     ('warplanes', 'armor', 'infantry'),
     ('warplanes', 'infantry', 'infantry'),
     ('armor', 'armor', 'armor'),
     ('armor', 'armor', 'infantry'),
     ('armor', 'infantry', 'infantry'),
     ('infantry', 'infantry', 'infantry')]


