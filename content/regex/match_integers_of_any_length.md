Title: Match Integers Of Any Length  
Slug: match_integers_of_any_length  
Summary: Match Integers Of Any Length  
Date: 2016-05-01 12:00  
Category: Regex  
Tags: Basics  
Authors: Chris Albon  

Based on: [StackOverflow](http://stackoverflow.com/questions/5917082/regular-expression-to-match-numbers-with-or-without-commas-and-decimals-in-text)

## Preliminaries


```python
# Load regex package
import re
```

## Create some text


```python
# Create a variable containing a text string
text = '21 scouts and 3 tanks fought against 4,003 protestors.'
```

## Apply regex


```python
# Find any character block that is a integer of any length
re.findall(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0', text)
```




    ['21', '3', '4,003']



Explanation from [Justin Morgan](http://stackoverflow.com/users/399649/justin-morgan)

    [1-9](?:\d{0,2}) #A sequence of 1-3 numerals not starting with 0
    (?:,\d{3})*      #Any number of three-digit groups, each preceded by a comma
    (?:\.\d*[1-9])?  #Optionally, a decimal point followed by any number of digits not ending in 0
    |                #OR...
    0?\.\d*[1-9]     #Only the decimal portion, optionally preceded by a 0
    |                #OR...
    0                #Zero.
