Title: Match US Phone Numbers  
Slug: match_us_phone_numbers  
Summary: Match US Phone Numbers  
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
text = 'My phone number is 415-333-3922. His phone number is 4239389283'
```

## Apply regex


```python
# Find any text that fits the regex
re.findall(r'\(?([2-9][0-8][0-9])\)?[-.●]?([2-9][0-9]{2})[-.●]?([0-9]{4})', text)
```




    [('415', '333', '3922'), ('423', '938', '9283')]


