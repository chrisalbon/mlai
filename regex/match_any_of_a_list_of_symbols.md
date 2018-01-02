Title: Match Any Of A List Of Characters  
Slug: match_any_of_a_list_of_symbols  
Summary: Match Any Of A List Of Characters  
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
# Find all instances of any vowel
re.findall(r'[aeiou]', text)
```




    ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o', 'e', 'a']


