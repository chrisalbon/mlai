Title: Match Words With A Certain Ending  
Slug: match_words_with_certain_ending  
Summary: Match Words With A Certain Ending  
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
text = 'Capitalism, Communism, Neorealism, Liberalism'
```

## Apply regex


```python
# Find any word ending in 'ism'
re.findall(r'\b\w*ism\b', text)

# Specific:
# \b     - start of the word
# \w*    - a word of any length
# ism\b  - with 'ism'at the end
```




    ['Capitalism', 'Communism', 'Neorealism', 'Liberalism']


