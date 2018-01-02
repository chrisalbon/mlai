Title: while Statement  
Slug: while_statements  
Summary: while Statement  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## A while loop loops while a condition is true, stops when the condition becomes false

### Import the random module


```python
import random
```

### Create a variable of the true number of deaths of an event


```python
deaths = 6
```

## Create a variable that is denotes if the while loop should keep running


```python
running = True
```

### while running is True


```python
while running:
    # Create a variable that randomly create a integer between 0 and 10.
    guess = random.randint(0,10)

    # if guess equals deaths,
    if guess == deaths:
        # then print this
        print('Correct!')
        # and then also change running to False to stop the script
        running = False
    # else if guess is lower than deaths
    elif guess < deaths:
        # then print this
        print('No, it is higher.')
    # if guess is none of the above
    else:
        # print this
        print('No, it is lower')
```

    No, it is higher.
    No, it is higher.
    Correct!


By the output, you can see that the while script keeping generating guesses and checking them until guess matches deaths, in which case the script stops.
