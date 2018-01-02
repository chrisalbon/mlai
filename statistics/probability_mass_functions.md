Title: Probability Mass Functions  
Slug: probability_mass_functions  
Summary: Probability Mass Functions in Python.    
Date: 2016-02-08 12:00  
Category: Statistics  
Tags: Basics
Authors: Chris Albon  

## Preliminaries


```python
# Load libraries
import matplotlib.pyplot as plt
```

## Create Data


```python
# Create some random integer data
data = [3,2,3,4,2,3,5,2,2,3,3,5,2,2,5,6,2,2,2,3,6,6,2,4,3,2,3]
```

## Create A Count Of Values


```python
# Create a dictionary to store the counts
count = {}

# For each value in the data
for observation in data:
    # An a key, value pair, with the observation being the key
    # and the value being +1
    count[observation] = count.get(observation, 0) + 1
```

## Normalize The Count To Between 0 and 1


```python
# Calculate the number of observations
n = len(data)

# Create a dictionary
probability_mass_function = {}

# For each unique value,
for unique_value, count in count.items():
    # Normalize the count by dividing by the length of data, add to the PMC dictionary
    probability_mass_function[unique_value] = count / n
```

## Visualize The PMF


```python
# Plot the probability mass function
plt.bar(list(probability_mass_function.keys()), probability_mass_function.values(), color='g')
plt.show()
```


![png](probability_mass_functions_files/probability_mass_functions_10_0.png)

