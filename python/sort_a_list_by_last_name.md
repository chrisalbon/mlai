Title: Sort A List Of Names By Last Name  
Slug: sort_a_list_by_last_name  
Summary: Sort A List Of Names By Last Name  
Date: 2016-06-25 12:00  
Category: Python  
Tags: Data Wrangling   
Authors: Chris Albon  

## Create a list of names


```python
commander_names = ["Alan Brooke", "George Marshall", "Frank Jack Fletcher", "Conrad Helfrich", "Albert Kesselring"] 
```

## Sort Alphabetically By Last Name

To complete the sort, we will combine three operations:

- `lambda x: x.split(" ")`, which is a function that takes a string `x` and breaks it up along each blank space. This outputs a list.
- `[-1]`, which takes the last element of a list.
- `sorted()`, which sorts a list.


```python
# Sort a variable called 'commander_names' by the last elements of each name.
sorted(commander_names, key=lambda x: x.split(" ")[-1])
```




    ['Alan Brooke',
     'Frank Jack Fletcher',
     'Conrad Helfrich',
     'Albert Kesselring',
     'George Marshall']


