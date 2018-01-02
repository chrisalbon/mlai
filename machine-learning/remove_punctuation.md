Title: Remove Punctuation  
Slug: remove_punctuation  
Summary: How to remove punctuation from unstructured text data for machine learning in Python.   
Date: 2016-09-08 12:00  
Category: Machine Learning  
Tags: Preprocessing Text
  
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
import string
import numpy as np
```

## Create Text Data


```python
# Create text
text_data = ['Hi!!!! I. Love. This. Song....', 
             '10000% Agree!!!! #LoveIT', 
             'Right?!?!']
```

## Remove Punctuation


```python
# Create function using string.punctuation to remove all punctuation
def remove_punctuation(sentence: str) -> str:
    return sentence.translate(str.maketrans('', '', string.punctuation))

# Apply function
[remove_punctuation(sentence) for sentence in text_data]
```




    ['Hi I Love This Song', '10000 Agree LoveIT', 'Right']


