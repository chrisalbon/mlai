Title: Match A Symbol  
Slug: match_a_symbol  
Summary: Match A Symbol  
Date: 2016-05-01 12:00  
Category: Regex  
Tags: Basics  
Authors: Chris Albon  

Based on: [Regular Expressions Cookbook](http://shop.oreilly.com/product/0636920023630.do)

## Preliminaries


```python
# Load regex package
import re
```

## Create some text


```python
# Create a variable containing a text string
text = '$100'
```

## Apply regex


```python
# Find all instances of the exact match '$'
re.findall(r'\$', text)
```




    ['$']


