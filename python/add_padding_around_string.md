Title: Add Padding Around String  
Slug: add_padding_around_string  
Summary: Add Padding Around String Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Create Some Text 


```python
text = 'Chapter 1'
```

## Add Padding Around Text 


```python
# Add Spaces Of Padding To The Left
format(text, '>20')
```




    '           Chapter 1'




```python
# Add Spaces Of Padding To The Right
format(text, '<20')
```




    'Chapter 1           '




```python
# Add Spaces Of Padding On Each Side
format(text, '^20')
```




    '     Chapter 1      '




```python
# Add * Of Padding On Each Side
format(text, '*^20')
```




    '*****Chapter 1******'


