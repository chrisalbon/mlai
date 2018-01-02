Title: Nesting Lists  
Slug: nesting_lists  
Summary: Nesting Lists  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  


```python
# Create a list of three nested lists, each with three items
state_regions = [['California', 'Oregon', 'Washington'],
        ['Texas','Georgia','Alabama'],
        ['Maine','Vermont','New York']]
```


```python
# View the list
state_regions
```




    [['California', 'Oregon', 'Washington'],
     ['Texas', 'Georgia', 'Alabama'],
     ['Maine', 'Vermont', 'New York']]




```python
# Print the second list's third item
state_regions[1][2]
```




    'Alabama'


