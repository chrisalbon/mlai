Title: Looping Over Two Lists  
Slug: looping_over_two_lists_using_Python  
Summary: Looping over two lists using Python  
Date: 2016-09-06 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon


```python
# Create a list of length 3:
armies = ['Red Army', 'Blue Army', 'Green Army']

# Create a list of length 4:
units = ['Red Infantry', 'Blue Armor','Green Artillery','Orange Aircraft']
```


```python
# For each element in the first list,
for army, unit in zip(armies, units):
    # Display the corresponding index element of the second list:
    print(army, 'has the following options:', unit)
```

    Red Army has the following options: Red Infantry
    Blue Army has the following options: Blue Armor
    Green Army has the following options: Green Artillery


Notice that the fourth item of the second list, `orange aircraft`, did not display.
