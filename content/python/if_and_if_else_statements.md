Title: if and if else  
Slug: if_and_if_else_statements  
Summary: if and if else  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

### Create a variable with the status of the conflict.

- 1 if the conflict is active
- 0 if the conflict is not active
- unknown if the status of the conflict is unknwon


```python
conflict_active = 1
```

### If the conflict is active print a statement


```python
if conflict_active == 1:
    print('The conflict is active.')
```

    The conflict is active.


### If the conflict is active print a statement, if not, print a different statement


```python
if conflict_active == 1:
    print('The conflict is active.')
else:
    print('The conflict is not active.')
```

    The conflict is active.


### If the conflict is active print a statement, if not, print a different statement, if unknown, state a third statement.


```python
if conflict_active == 1:
    print('The conflict is active.')
elif conflict_active == 'unknown':
    print('The status of the conflict is unknown')
else:
    print('The conflict is not active.')
```

    The conflict is active.

