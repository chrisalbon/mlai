Title: Match US and UK Spellings  
Slug: match_us_uk_spellings  
Summary: Match US and UK Spellings  
Date: 2016-05-01 12:00  
Category: Regex  
Tags: Basics  
Authors: Chris Albon  

Source: [Regular Expressions Cookbook](http://shop.oreilly.com/product/0636920023630.do)

## Preliminaries


```python
# Load regex package
import re
```

## Create some text


```python
# Create a variable containing a text string
text = 'It\s center and not centre.'
```

## Apply regex


```python
# Find any ISBN-10 or ISBN-13 number
re.findall(r'\bcent(?:er|re)\b', text)
```




    ['center', 'centre']


