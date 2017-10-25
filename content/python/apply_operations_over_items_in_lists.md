Title: Apply Operations Over Items In A List  
Slug: apply_operations_over_items_in_lists  
Summary: Apply Operations Over Items In A List  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Method 1: map()


```python
# Create a list of casualties from battles
battleDeaths = [482, 93, 392, 920, 813, 199, 374, 237, 244]
```


```python
# Create a function that updates all battle deaths by adding 100
def updated(x): return x + 100
```


```python
# Create a list that applies updated() to all elements of battleDeaths
list(map(updated, battleDeaths))
```




    [582, 193, 492, 1020, 913, 299, 474, 337, 344]



## Method 2: for x in y


```python
# Create a list of deaths
casualties = [482, 93, 392, 920, 813, 199, 374, 237, 244]
```


```python
# Create a variable where we will put the updated casualty numbers
casualtiesUpdated = []
```


```python
# Create a function that for each item in casualties, adds 10
for x in casualties:
    casualtiesUpdated.append(x + 100)
```


```python
# View casualties variables
casualtiesUpdated
```




    [582, 193, 492, 1020, 913, 299, 474, 337, 344]



## Method 3: lambda functions


```python
# Map the lambda function x() over casualties
list(map((lambda x: x + 100), casualties))
```




    [582, 193, 492, 1020, 913, 299, 474, 337, 344]


