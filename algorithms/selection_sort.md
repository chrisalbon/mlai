Title: Selection Sort  
Slug: selection_sort  
Summary: Selection Sort Using Python.  
Date: 2016-01-30 12:00  
Category: Algorithms  
Tags: Basics  
Authors: Chris Albon  
    
This might not be the most efficient implementation of the selection sort algorithm. However, it is the one that closely matches how the algorithm is explained:

1. Pick up the first card (if this was a deck of cards).
2. Compare the card in your hand to each other card in turn
3. If a smaller card is found, swap the cards (so the smaller card is now in your hand).
4. When you get to the last card, put the card in your hand into a separate pile.
5. Repeat steps 1-4 until there are no more cards in the original deck

## Create A Sequence


```python
alist = [8,5,3,6,2,1,9,4,7]
alist
```




    [8, 5, 3, 6, 2, 1, 9, 4, 7]



## Create A Selection Sort Algorithm


```python
# Define a function that takes an unsorted list,
def selection_sort(alist):
    
    # Create a new list containing the values from the inputed list
    unsorted_sequence = alist[:]
    
    # Create a list where we will place the sorted values
    sorted_sequence = []
        
    # While there are still values in the unsorted sequence:
    while len(unsorted_sequence) > 0:
        # For each value in the unsorted sequence,
        for i, _ in enumerate(unsorted_sequence):

            # Assume it is the smallest value
            smallest_value_index = i

            # Compare it which each other value in the unsorted list
            for i, _ in enumerate(unsorted_sequence):

                # If a smaller value is found
                if unsorted_sequence[smallest_value_index] > unsorted_sequence[i]:
                    
                    # Swap the two values so the new value is the one we think is the smallest
                    smallest_value_index, i = i, smallest_value_index

            # When we get to the end of the sequence, remove the smallest valued card
            smallest_value = unsorted_sequence.pop(smallest_value_index)

            # And add it to our sequence of sorted values
            sorted_sequence.append(smallest_value)

            # Print the sorted sequence
            print('Sorted sequence so far:', sorted_sequence)
```


```python
# Run the selection sort
selection_sort(alist)
```

    Sorted sequence so far: [1]
    Sorted sequence so far: [1, 2]
    Sorted sequence so far: [1, 2, 3]
    Sorted sequence so far: [1, 2, 3, 4]
    Sorted sequence so far: [1, 2, 3, 4, 5]
    Sorted sequence so far: [1, 2, 3, 4, 5, 6]
    Sorted sequence so far: [1, 2, 3, 4, 5, 6, 7]
    Sorted sequence so far: [1, 2, 3, 4, 5, 6, 7, 8]
    Sorted sequence so far: [1, 2, 3, 4, 5, 6, 7, 8, 9]

