Title: Match A Unicode Character  
Slug: match_a_unicode_character  
Summary: Match A Unicode Character  
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
text = 'Microsoft™.'
```

## Apply regex


```python
# Find any unicode character for a trademark
re.findall(r'\u2122', text)
```




    ['™']


