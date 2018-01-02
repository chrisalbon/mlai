Title: Unpacking Function Arguments  
Slug: unpacking_function_arguments  
Summary: Unpacking Function Arguments in Python.    
Date: 2016-01-23 12:00  
Category: Python  
Tags: Basics    
Authors: Chris Albon  

Interesting in learning more? Check out [Fluent Python](http://amzn.to/2jYU506)

## Create Argument Objects


```python
# Create a dictionary of arguments
argument_dict = {'a':'Alpha', 'b':'Bravo'}

# Create a list of arguments
argument_list = ['Alpha', 'Bravo']
```

## Create A Simple Function


```python
# Create a function that takes two inputs
def simple_function(a, b):
    # and prints them combined
    return a + b
```

## Run the Function With Unpacked Arguments


```python
# Run the function with the unpacked argument dictionary
simple_function(**argument_dict)
```




    'AlphaBravo'




```python
# Run the function with the unpacked argument list
simple_function(*argument_list)
```




    'AlphaBravo'


