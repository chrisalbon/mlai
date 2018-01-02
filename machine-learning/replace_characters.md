Title: Replace Characters  
Slug: replace_characters  
Summary: How to remove characters to clean unstructured text data for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Text
Authors: Chris Albon

## Preliminaries


```python
# Import library
import re
```

## Create Text


```python
# Create text
text_data = ['Interrobang. By Aishwarya Henriette',
             'Parking And Going. By Karl Gautier',
             'Today Is The night. By Jarek Prakash']
```

## Replace Character (Method 1)


```python
# Remove periods
remove_periods = [string.replace('.', '') for string in text_data]

# Show text
remove_periods
```




    ['Interrobang By Aishwarya Henriette',
     'Parking And Going By Karl Gautier',
     'Today Is The night By Jarek Prakash']



## Replace Character (Method 2)


```python
# Create function
def replace_letters_with_X(string: str) -> str:
    return re.sub(r'[a-zA-Z]', 'X', string)

# Apply function
[replace_letters_with_X(string) for string in remove_periods]
```




    ['XXXXXXXXXXX XX XXXXXXXXX XXXXXXXXX',
     'XXXXXXX XXX XXXXX XX XXXX XXXXXXX',
     'XXXXX XX XXX XXXXX XX XXXXX XXXXXXX']


