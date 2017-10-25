Title: Insertion Sort  
Slug: insertion_sort  
Summary: Insertion Sort Using Python.  
Date: 2016-01-30 12:00  
Category: Algorithms  
Tags: Basics  
Authors: Chris Albon  

## Create A Sequence


```python
alist = [8,5,3,6,2,1,9,4,7]
alist
```




    [8, 5, 3, 6, 2, 1, 9, 4, 7]



## Create A Selection Sort Algorithm


```python
# Define an function that takes a list
def insertion_sort(alist):
    
    # Create a sequence from the argument list
    sequence = alist[:]
    
    # Get the length of the list
    n = len(sequence)
    
    # For 1 through the length for the sequence:
    for i in range(1, n):
        
        # save the value of the card
        value = sequence[i]
        
        # save the current position of the card
        position = i
        
        # while the card is not the first card and is smaller than the card to it's left:
        while position > 0 and value < sequence[position - 1]:
            # the card overwrites the card to the left
            sequence[position] = sequence[position - 1]
            # And we move on to the next position
            position -= 1
            
        # When we have found the right position (meaning the while loop is false)
        # put the card in its correct spot in the deck
        sequence[position] = value
        
        # View the deck so far
        print(sequence)
```


```python
# Run the sort
insertion_sort(alist)
```

    [5, 8, 3, 6, 2, 1, 9, 4, 7]
    [3, 5, 8, 6, 2, 1, 9, 4, 7]
    [3, 5, 6, 8, 2, 1, 9, 4, 7]
    [2, 3, 5, 6, 8, 1, 9, 4, 7]
    [1, 2, 3, 5, 6, 8, 9, 4, 7]
    [1, 2, 3, 5, 6, 8, 9, 4, 7]
    [1, 2, 3, 4, 5, 6, 8, 9, 7]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

