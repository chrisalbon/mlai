Title: Regular Expression Basics  
Slug: regular_expressions_basics  
Summary: Regular Expression Basics  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

### Import the regex (re) package


```python
import re
```

### Import sys


```python
import sys
```

### Create a simple text string.


```python
text = 'The quick brown fox jumped over the lazy black bear.'
```

### Create a pattern to match


```python
three_letter_word = '\w{3}'
```

### Convert the string into a regex object


```python
pattern_re = re.compile(three_letter_word); pattern_re
```




    re.compile(r'\w{3}', re.UNICODE)



### Does a three letter word appear in text?


```python
re_search = re.search('..own', text)
```

### If the search query is at all true,


```python
if re_search:
    # Print the search results
    print(re_search.group())
```

    brown


## re.match

re.match() is for matching ONLY the beginning of a string or the whole string
For anything else, use re.search

### Match all three letter words in text


```python
re_match = re.match('..own', text)
```

### If re_match is true, print the match, else print "No Matches"


```python
if re_match:
    # Print all the matches
    print(re_match.group())
else:
    # Print this
    print('No matches')
```

    No matches


## re.split

### Split up the string using "e" as the seperator.


```python
re_split = re.split('e', text); re_split
```




    ['Th', ' quick brown fox jump', 'd ov', 'r th', ' lazy black b', 'ar.']



## re.sub

Replaces occurrences of the regex pattern with something else

The "3" references to the maximum number of substitutions to make.

### Substitute the first three instances of "e" with "E", then print it


```python
re_sub = re.sub('e', 'E', text, 3); print(re_sub)
```

    ThE quick brown fox jumpEd ovEr the lazy black bear.

