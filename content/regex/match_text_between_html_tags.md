Title: Match Text Between HTML Tags  
Slug: match_text_between_html_tags  
Summary: Match Text Between HTML Tags  
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
text = '<p>The quick brown fox.</p><p>The lazy brown bear.</p>'
```

## Apply regex


```python
# Find any text between '<p>' and '</p>'
re.findall(r'<p>(.*?)</p>', text)
```




    ['The quick brown fox.', 'The lazy brown bear.']


