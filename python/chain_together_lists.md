Title: Chain Together Lists  
Slug: chain_together_lists  
Summary: Chain Together Lists Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Preliminaries


```python
from itertools import chain
```

## Create Two Lists


```python
# Create a list of allies
allies = ['Spain', 'Germany', 'Namibia', 'Austria']

# Create a list of enemies
enemies = ['Mexico', 'United Kingdom', 'France']
```

## Iterate Over Both Lists As A Single Sequence


```python
# For each country in allies and enemies
for country in chain(allies, enemies):
    # print the country
    print(country)
```

    Spain
    Germany
    Namibia
    Austria
    Mexico
    United Kingdom
    France

