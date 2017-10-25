Title: Functions Vs. Generators  
Slug: functions_vs_generators  
Summary: Functions Vs. Generators in Python.    
Date: 2016-01-23 12:00  
Category: Python  
Tags: Basics    
Authors: Chris Albon  

Interesting in learning more? Check out [Fluent Python](http://amzn.to/2jYU506)

## Create A Function


```python
# Create a function that
def function(names):
    # For each name in a list of names
    for name in names:
        # Returns the name
        return name
```


```python
# Create a variable of that function
students = function(['Abe', 'Bob', 'Christina', 'Derek', 'Eleanor'])
```


```python
# Run the function
students
```




    'Abe'



Now we have a problem, we were only returned the name of the first student. Why? Because the function only ran the `for name in names` iteration once!

## Create A Generator

A generator is a function, but instead of returning the `return`, instead returns an iterator. The generator below is exactly the same as the function above except I have replaced `return` with `yield` (which defines whether a function with a regular function or a generator function).


```python
# Create a generator that
def generator(names):
    # For each name in a list of names
    for name in names:
        # Yields a generator object
        yield name
```


```python
# Same as above, create a variable for the generator
students = generator(['Abe', 'Bob', 'Christina', 'Derek', 'Eleanor'])
```

Everything has been the same so far, but now things get interesting. Above when we ran `students` when it was a function, it returned one name. However, now that `students` refers to a generator, it yields a generator object of names!


```python
# Run the generator
students
```




    <generator object generator at 0x104837a40>



What can we do this a generator object? A lot! As a generator `students` will can each student in the list of students:


```python
# Return the next student
next(students)
```




    'Abe'




```python
# Return the next student
next(students)
```




    'Bob'




```python
# Return the next student
next(students)
```




    'Christina'



It is interesting to note that if we use list(students) we can see all the students still remaining in the generator object's iteration:


```python
# List all remaining students in the generator
list(students)
```




    ['Derek', 'Eleanor']


