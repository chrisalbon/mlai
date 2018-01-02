Title: Exiting A Loop  
Slug: exiting_a_loop_python  
Summary: Exiting a loop in Python  
Date: 2016-09-06 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon

## Create A List


```python
# Create a list:
armies = ['Red Army', 'Blue Army', 'Green Army']
```

## Breaking Out Of A For Loop


```python
for army in armies:
    print(army)
    if army == 'Blue Army':
        print('Blue Army Found! Stopping.')
        break
```

    Red Army
    Blue Army
    Blue Army Found! Stopping.


Notice that the loop stopped after the conditional if statement was satisfied.

## Exiting If Loop Completed

A loop will exit when completed, but using an `else` statement we can add an action at the conclusion of the loop if it hasn't been exited earlier.


```python
for army in armies:
    print(army)
    if army == 'Orange Army':
        break
else:
    print('Looped Through The Whole List, No Orange Army Found')
```

    Red Army
    Blue Army
    Green Army
    Looped Through The Whole List, No Orange Army Found

