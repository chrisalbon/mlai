Title: Match ZIP Codes  
Slug: match_zip_codes  
Summary: Match ZIP Codes  
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
text = '3829 South Ave Street, Pheonix, AZ 34923'
```

## Apply regex


```python
# Find any ISBN-10 or ISBN-13 number
re.findall(r'[0-9]{5}(?:-[0-9]{4})?', text)
```




    ['34923']


