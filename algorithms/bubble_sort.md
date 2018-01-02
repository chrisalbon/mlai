Title: Bubble Sort  
Slug: bubble_sort  
Summary: Bubble Sort Using Python.  
Date: 2016-01-30 12:00  
Category: Algorithms  
Tags: Basics  
Authors: Chris Albon  
    
Want to learn more? Check out [Data Structures and Algorithms in Python](http://amzn.to/2kjkqWQ)

## Create A Sequence


```python
unsorted_list = [8,5,3,6,2,1,9,4,7]
unsorted_list
```




    [8, 5, 3, 6, 2, 1, 9, 4, 7]



## Create A Bubble Sort Function


```python
# Define a function that takes an unsorted sequence
def bubble_sort(unsorted_list):
    
    # Create a new list containing the values from the inputed list
    sequence = unsorted_list[:]
    
    # For each value of the sequence (epochs),
    for i, _ in enumerate(sequence):
        # For each value of the sequence,
        for i, _ in enumerate(sequence):
            # Try
            try:
                # If a value is greater than the value that follows it
                if sequence[i] > sequence[i+1]:
                    # Swap the values in the sequence
                    sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
            # If you raise an index error, you are at the end of the sequence,
            except IndexError:
                # So ignore the error and continue with iteration
                continue
                
        # Print the sequence afer each epoch
        print(sequence)
```


```python
# Run the function
bubble_sort(unsorted_list)
```

    [5, 3, 6, 2, 1, 8, 4, 7, 9]
    [3, 5, 2, 1, 6, 4, 7, 8, 9]
    [3, 2, 1, 5, 4, 6, 7, 8, 9]
    [2, 1, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

