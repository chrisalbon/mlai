Title: Flatten Lists Of Lists  
Slug: flatten_list_of_lists  
Summary: Flatten Lists Of Lists  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# Create a list containing three lists of names
list_of_lists = [['Amy','Betty','Cathryn','Dana'], 
                 ['Elizabeth','Fay','Gora'], 
                  ['Heidi','Jane','Kayley']]
```


```python
# For each element in list_of_lists, take each element in the list
flattened_list = [i for row in list_of_lists for i in row]
```


```python
# View the flattened list
flattened_list
```




    ['Amy',
     'Betty',
     'Cathryn',
     'Dana',
     'Elizabeth',
     'Fay',
     'Gora',
     'Heidi',
     'Jane',
     'Kayley']


