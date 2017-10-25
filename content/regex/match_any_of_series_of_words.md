Title: Match Any Of A Series Of Words  
Slug: match_any_of_series_of_words  
Summary: Match Any Of A Series Of Words  
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
text = 'The quick brown fox jumped over the lazy brown bear.'
```

## Apply regex


```python
# Find any of fox, snake, or bear
re.findall(r'\b(fox|snake|bear)\b', text)
```




    ['fox', 'bear']


