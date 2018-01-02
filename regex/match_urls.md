Title: Match URLs  
Slug: match_urls  
Summary: Match URLs  
Date: 2016-05-01 12:00  
Category: Regex  
Tags: Basics  
Authors: Chris Albon  

Source: [StackOverflow](http://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string)

## Preliminaries


```python
# Load regex package
import re
```

## Create some text


```python
# Create a variable containing a text string
text = 'My blog is http://www.chrisalbon.com and not http://chrisalbon.com'
```

## Apply regex


```python
# Find any ISBN-10 or ISBN-13 number
re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', text)
```




    [('http', 'www.chrisalbon.com', ''), ('http', 'chrisalbon.com', '')]


