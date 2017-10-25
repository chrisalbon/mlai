Title: Match Times  
Slug: match_times  
Summary: Match Times  
Date: 2016-05-01 12:00  
Category: Regex  
Tags: Basics  
Authors: Chris Albon  

Based on: [StackOverflow](http://stackoverflow.com/questions/18715392/javascript-regex-validate-time-with-am-and-pm)

## Preliminaries


```python
# Load regex package
import re
```

## Create some text


```python
# Create a variable containing a text string
text = 'Chris: 12:34am. Steve: 16:30'
```

## Apply regex


```python
# Find any text that fits the regex
re.findall(r'([0-1]\d:[0-5]\d)\s*(?:AM|PM)?', text)
```




    ['12:34', '16:30']


