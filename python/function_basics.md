Title: Function Basics  
Slug: function_basics  
Summary: Function Basics   
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Create Function Called print_max


```python
def print_max(x, y):
    # if a is larger than b
    if x > y:
        # then print this
        print(x, 'is maximum')
    # if a is equal to b
    elif x == y:
        # print this
        print(x, 'is equal to', y)
    # otherwise
    else:
        # print this
        print(y, 'is maximum')
```

## Run Function With Two Arguments


```python
print_max(3,4)
```

    4 is maximum


Note: By default, variables created within functions are local to the function. But you can create a global function that IS defined outside the function.

## Create Variable


```python
x = 50
```

## Create Function Called Func


```python
# Create function
def func():
    # Create a global variable called x
    global x

    # Print this
    print('x is', x)
    
    # Set x to 2.
    x = 2
    
    # Print this
    print('Changed global x to', x)
```

## Run func()


```python
func()
```

    x is 50
    Changed global x to 2


## Print x


```python
x
```




    2



## Create Function Say() Displaying x with default value of 1


```python
# Create function
def say(x, times = 1, times2 = 3):
    print(x * times, x * times2)

# Run the function say() with the default values
say('!')

# Run the function say() with the non-default values of 5 and 10
say('!', 5, 10)
```

    ! !!!
    !!!!! !!!!!!!!!!


## VarArgs Parameters (i.e. unlimited number of parameters)
- \* denotes that all positonal arguments from that point to next arg are used
- \** dnotes that all keyword arguments from that point to the next arg are used


```python
# Create a function called total() with three parameters
def total(initial=5, *numbers, **keywords):
    # Create a variable called count that takes it's value from initial
    count = initial
    # for each item in numbers
    for number in numbers:
        # add count to that number
        count += number
    # for each item in keywords
    for key in keywords:
        # add count to keyword's value
        count += keywords[key]
    # return counts
    return count

# Run function
total(10, 1, 2, 3, vegetables=50, fruits=100)
```




    166


