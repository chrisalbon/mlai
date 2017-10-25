Title: Enumerate A List  
Slug: enumerate_a_list  
Summary: Enumerate A List  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  


```python
# Create a list of strings
data = ['One','Two','Three','Four','Five']
```


```python
# For each item in the enumerated variable, data
for item in enumerate(data):
    # Print the whole enumerated element
    print(item)
    # Print only the value (not the index number)
    print(item[1])
```

    (0, 'One')
    One
    (1, 'Two')
    Two
    (2, 'Three')
    Three
    (3, 'Four')
    Four
    (4, 'Five')
    Five

