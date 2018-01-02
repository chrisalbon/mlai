Title: Strip Whitespace  
Slug: stripe_whitespace  
Summary: How to strip whitespace to clean unstructured text data for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Text
  
Authors: Chris Albon

## Create Text


```python
# Create text
text_data = ['   Interrobang. By Aishwarya Henriette     ',
             'Parking And Going. By Karl Gautier',
             '    Today Is The night. By Jarek Prakash   ']
```

## Remove Whitespace


```python
# Strip whitespaces
strip_whitespace = [string.strip() for string in text_data]

# Show text
strip_whitespace
```




    ['Interrobang. By Aishwarya Henriette',
     'Parking And Going. By Karl Gautier',
     'Today Is The night. By Jarek Prakash']


