Title: Variance And Standard Deviation   
Slug: variance_and_standard_deviation  
Summary: Calculating Variance And Standard Deviation in Python.    
Date: 2016-02-08 12:00  
Category: Statistics  
Tags: Basics
Authors: Chris Albon  

## Preliminary


```python
# Import data
import math
```

## Create Data


```python
# Create list of values
data = [3,2,3,4,2,3,5,2,2,33,3,5,2,2,5,6,62,2,2,3,6,6,2,23,3,2,3]
```

## Calculate Population Variance

Variance is a measurement of the spread of a data's distribution. The higher the variance, the more "spread out" the data points are. Variance, commonly denoted as $S^{2}$, is calculated like this:

$$ \text{Population Variance} = S_n^{2} = \frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^{2}$$

$$ \text{Sample Variance} = S_{n-1}^{2} = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^{2}$$

Where $n$ is the number of observations, $\bar{x}$ is the mean of the observations, and $x_i-\bar{x}$ is an individual observation's from the mean of the data. Note that if we were estimating the variance of a population based on a sample from that population, we should use the second equation, replacing $n$ with $n-1$.


```python
# Calculate n
n = len(data)

# Calculate the mean
mean = sum(data)/len(data)

# Create a list of all deviations from the mean
all_deviations_from_mean_squared = []

# For each observation in the data
for observation in data:
    
    # Calculate the deviation from the mean
    deviation_from_mean = (observation - mean)
    
    # Square it
    deviation_from_mean_squared = deviation_from_mean**2
    
    # Add the result to our list
    all_deviations_from_mean_squared.append(deviation_from_mean_squared)

# Sum all the squared deviations in our list    
sum_of_deviations_from_mean_squared = sum(all_deviations_from_mean_squared)

# Divide by n
population_variance = sum_of_deviations_from_mean_squared/n

# Show variance
population_variance    
```




    160.78463648834017



## Calculate Population Standard Deviation

Standard deviation is just the square root of the variance.


```python
# Find the square root of the population variance
population_standard_deviation = math.sqrt(population_variance)

# Print the populaton standard deviation
population_standard_deviation
```




    12.68008818929664


