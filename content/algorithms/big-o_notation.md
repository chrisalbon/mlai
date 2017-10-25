Title: Big-O Notation  
Slug: big-o_notation  
Summary: Using Python.  
Date: 2016-05-01 12:00  
Category: Algorithms  
Tags: Basics  
Authors: Chris Albon  
    
Want to learn more? Check out [Data Structures and Algorithms in Python](http://amzn.to/2kjkqWQ)

Big-O notation is used to classify the worst-case "speed" of an algorithm by looking at the order of magnitude of execution time.

From best to worst, some common Big-O's are: 

- O(1)
- O(log n)
- O(n)
- O(n log n)
- O(n<sup>2</sup>)
- O(n<sup>3</sup>)
- O(2<sup>n</sup>)

Below are some examples of a few of these.

## Create Data


```python
# Create a list 100 elements long
n = list(range(100))
```

## O(1) - Constant Time-Complexity

The length of `n` has no bearing on the number of steps required to complete the function. This is the ideal.


```python
# Create a function that, regardless of the length of n,
def constant(n):
    # returns 1
    return 'Number of operations: ' + str(1)
```


```python
constant(n)
```




    'Number of operations: 1'



## O(log n) - Logarithmic Time-Complexity


```python
# Create a function that
def logarithmic(n):
    # Creates a list of the operations performed
    operations = []
    
    # While n is longer than 1, repeat this:
    while len(n) > 1:
        # Find half the lengh of n
        half_length = int(len(n)/2)
        
        # Add half the values of n to operations
        operations = operations + n[0:half_length]
        
        # make n half the length of itself, then restart the loop
        n = n[0:half_length]
        
    # Return the number of operations
    return 'Number of operations: ' + str(len(operations))
```


```python
logarithmic(n)
```




    'Number of operations: 97'



## O(n) - Linear Time-Complexity


```python
def linear(n):
    # Creates a list of the operations performed
    operations = []
    
    # For every item in n
    for item in n:
        # Add the item to operations
        operations.append(item)
        
    # Return the number of operations
    return 'Number of operations: ' +  str(len(operations))
```


```python
linear(n)
```




    'Number of operations: 100'



## O(n<sup>2</sup>) - Quadratic Time-Complexity


```python
def quadratic(n):
    # Creates a list of the operations performed
    operations = []
    
    # For every item in n,
    for i in n:
        # Look at every item item in n
        for j in n:
            # and append it to operations
            operations.append(j)
            
    # Return the number of operations
    return 'Number of operations: ' +  str(len(operations))
```


```python
quadratic(n)
```




    'Number of operations: 10000'


