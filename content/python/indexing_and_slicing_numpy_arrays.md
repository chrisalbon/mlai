Title: Indexing And Slicing Numpy Arrays  
Slug: indexing_and_slicing_numpy_arrays  
Summary: Indexing And Slicing Numpy Arrays  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Slicing Arrays

### Explanation Of Broadcasting

Unlike many other data types, slicing an array into a new variable means that any chances to that new variable are broadcasted to the original variable. Put other way, a slice is a hotlink to the original array variable, not a seperate and independent copy of it.


```python
# Import Modules
import numpy as np
```


```python
# Create an array of battle casualties from the first to the last battle
battleDeaths = np.array([1245, 2732, 3853, 4824, 5292, 6184, 7282, 81393, 932, 10834])
```


```python
# Divide the array of battle deaths into start, middle, and end of the war
warStart = battleDeaths[0:3]; print('Death from battles at the start of war:', warStart)
warMiddle = battleDeaths[3:7]; print('Death from battles at the middle of war:', warMiddle)
warEnd = battleDeaths[7:10]; print('Death from battles at the end of war:', warEnd)
```

    Death from battles at the start of war: [1245 2732 3853]
    Death from battles at the middle of war: [4824 5292 6184 7282]
    Death from battles at the end of war: [81393   932 10834]



```python
# Change the battle death numbers from the first battle
warStart[0] = 11101
```


```python
# View that change reflected in the warStart slice of the battleDeaths array
warStart
```




    array([11101,  2732,  3853])




```python
# View that change reflected in (i.e. "broadcasted to) the original battleDeaths array
battleDeaths
```




    array([11101,  2732,  3853,  4824,  5292,  6184,  7282, 81393,   932, 10834])



## Indexing Arrays

Note: This multidimensional array behaves like a dataframe or matrix (i.e. columns and rows)


```python
# Create an array of regiment information
regimentNames = ['Nighthawks', 'Sky Warriors', 'Rough Riders', 'New Birds']
regimentNumber = [1, 2, 3, 4]
regimentSize = [1092, 2039, 3011, 4099]
regimentCommander = ['Mitchell', 'Blackthorn', 'Baker', 'Miller']

regiments = np.array([regimentNames, regimentNumber, regimentSize, regimentCommander])
regiments
```




    array([['Nighthawks', 'Sky Warriors', 'Rough Riders', 'New Birds'],
           ['1', '2', '3', '4'],
           ['1092', '2039', '3011', '4099'],
           ['Mitchell', 'Blackthorn', 'Baker', 'Miller']], 
          dtype='<U12')




```python
# View the first column of the matrix
regiments[:,0]
```




    array(['Nighthawks', '1', '1092', 'Mitchell'], 
          dtype='<U12')




```python
# View the second row of the matrix
regiments[1,]
```




    array(['1', '2', '3', '4'], 
          dtype='<U12')




```python
# View the top-right quarter of the matrix
regiments[:2,2:]
```




    array([['Rough Riders', 'New Birds'],
           ['3', '4']], 
          dtype='<U12')


