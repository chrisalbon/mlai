Title: Match Dates  
Slug: match_dates  
Summary: Match Dates  
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
text = 'My birthday is 09/15/1983. My brother\'s birthday is 01/01/01. My other two brothers have birthdays of 9/3/2001 and 09/1/83.'
```

## Apply regex


```python
# Find any text that fits the regex
re.findall(r'\b[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}\b', text)
```




    ['09/15/1983', '01/01/01', '9/3/2001', '09/1/83']


