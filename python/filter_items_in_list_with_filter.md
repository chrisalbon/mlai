Title: Selecting Items In A List With Filters  
Slug: filter_items_in_list_with_filter  
Summary: Selecting Items In A List With Filters  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# Create an list of items denoting the number of soldiers in each regiment, view the list
regimentSize = (5345, 6436, 3453, 2352, 5212, 6232, 2124, 3425, 1200, 1000, 1211); regimentSize
```




    (5345, 6436, 3453, 2352, 5212, 6232, 2124, 3425, 1200, 1000, 1211)



## One-line Method

This line of code does the same thing as the multiline method below, it is just more compact (but also more complicated to understand.


```python
# Create a list called smallRegiments that filters regimentSize to 
# find all items that fulfill the lambda function (which looks for all items under 2500).
smallRegiments = list(filter((lambda x: x < 2500), regimentSize)); smallRegiments
```




    [2352, 2124, 1200, 1000, 1211]



## Multi-line Method

The ease with interpreting what is happening, I've broken down the one-line filter method into multiple steps, one per line of code. This appears below.


```python
# Create a lambda function that looks for things under 2500
lessThan2500Filter = lambda x: x < 2500
```


```python
# Filter regimentSize by the lambda function filter
filteredRegiments = filter(lessThan2500Filter, regimentSize)
```


```python
# Convert the filter results into a list
smallRegiments = list(filteredRegiments)
```




    [2352, 2124, 1200, 1000, 1211]



## For Loop Equivalent

This for loop does the same as both methods above, except it uses a for loop.

### Create a for loop that go through each item of a list and finds items under 2500


```python
# Create a variable for the results of the loop to be placed
smallRegiments_2 = []

# for each item in regimentSize,
for x in regimentSize:
    # look if the item's value is less than 2500
    if x < 2500:
        # if true, add that item to smallRegiments_2
        smallRegiments_2.append(x)
```


```python
# View the smallRegiment_2 variable
smallRegiments_2
```




    [2352, 2124, 1200, 1000, 1211]


