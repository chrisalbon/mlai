Title: Sort A List Of Strings By Length 
Slug: sort_a_list_of_strings_by_length
Summary: Sort A List Of Strings By Length 
Date: 2016-06-25 12:00  
Category: Python  
Tags: Data Wrangling   
Authors: Chris Albon  

## Create a list of names


```python
commander_names = ["Alan Brooke", "George Marshall", "Frank Jack Fletcher", "Conrad Helfrich", "Albert Kesselring"] 
```

## Sort Alphabetically By Length

To complete the sort, we will combine two operations:

- `lambda x: len(x)`, which returns the length of each string.
- `sorted()`, which sorts a list.


```python
# Sort a variable called 'commander_names' by the length of each string
sorted(commander_names, key=lambda x: len(x))
```




    ['Alan Brooke',
     'George Marshall',
     'Conrad Helfrich',
     'Albert Kesselring',
     'Frank Jack Fletcher']


