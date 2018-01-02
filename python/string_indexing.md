Title: String Indexing  
Slug: string_indexing  
Summary: String Indexing  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

### Create a string


```python
string = 'Strings are defined as ordered collections of characters.'
```

### Print the entire string


```python
string[:]
```




    'Strings are defined as ordered collections of characters.'



### Print the first three characters


```python
string[0:3]
```




    'Str'



### Print the first three characters


```python
string[:3]
```




    'Str'



### Print the last three characters


```python
string[-3:]
```




    'rs.'



### Print the third to fifth character


```python
string[2:5]
```




    'rin'



### Print the first to the tenth character, skipping every other character


```python
string[0:10:2]
```




    'Srnsa'



### Print the string in reverse


```python
string[::-1]
```




    '.sretcarahc fo snoitcelloc deredro sa denifed era sgnirtS'


