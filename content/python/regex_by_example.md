Title: Regular Expression By Example  
Slug: regex_by_example  
Summary: Regular Expression By Example  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

This tutorial is based on: [http://www.tutorialspoint.com/python/python_reg_expressions.htm](http://www.tutorialspoint.com/python/python_reg_expressions.htm)


```python
# Import regex
import re
```


```python
# Create some data
text = 'A flock of 120 quick brown foxes jumped over 30 lazy brown, bears.'
```

### ^ Matches beginning of line.


```python
re.findall('^A', text)
```




    ['A']



### $ Matches end of line.


```python
re.findall('bears.$', text)
```




    ['bears.']



### . Matches any single character except newline.


```python
re.findall('f..es', text)
```




    ['foxes']



### [...] Matches any single character in brackets.


```python
# Find all vowels
re.findall('[aeiou]', text)
```




    ['o', 'o', 'u', 'i', 'o', 'o', 'e', 'u', 'e', 'o', 'e', 'a', 'o', 'e', 'a']



### [# ^...] Matches any single character not in brackets


```python
# Find all characters that are not lower-case vowels
re.findall('[^aeiou]', text)
```




    ['A',
     ' ',
     'f',
     'l',
     'c',
     'k',
     ' ',
     'f',
     ' ',
     '1',
     '2',
     '0',
     ' ',
     'q',
     'c',
     'k',
     ' ',
     'b',
     'r',
     'w',
     'n',
     ' ',
     'f',
     'x',
     's',
     ' ',
     'j',
     'm',
     'p',
     'd',
     ' ',
     'v',
     'r',
     ' ',
     '3',
     '0',
     ' ',
     'l',
     'z',
     'y',
     ' ',
     'b',
     'r',
     'w',
     'n',
     ',',
     ' ',
     'b',
     'r',
     's',
     '.']



### a | b Matches either a or b.


```python
re.findall('a|A', text)
```




    ['A', 'a', 'a']



### (re) Groups regular expressions and remembers matched text.


```python
# Find any instance of 'fox'
re.findall('(foxes)', text)
```




    ['foxes']



### \w Matches word characters.


```python
# Break up string into five character blocks
re.findall('\w\w\w\w\w', text)
```




    ['flock', 'quick', 'brown', 'foxes', 'jumpe', 'brown', 'bears']



### \W Matches nonword characters.


```python
re.findall('\W\W', text)
```




    [', ']



### \s Matches whitespace. Equivalent to [\t\n\r\f].


```python
re.findall('\s', text)
```




    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']



### \S Matches nonwhitespace.


```python
re.findall('\S\S', text)
```




    ['fl',
     'oc',
     'of',
     '12',
     'qu',
     'ic',
     'br',
     'ow',
     'fo',
     'xe',
     'ju',
     'mp',
     'ed',
     'ov',
     'er',
     '30',
     'la',
     'zy',
     'br',
     'ow',
     'n,',
     'be',
     'ar',
     's.']



### \d Matches digits. Equivalent to [0-9].


```python
re.findall('\d\d\d', text)
```




    ['120']



### \D Matches nondigits.


```python
re.findall('\D\D\D\D\D', text)
```




    ['A flo',
     'ck of',
     ' quic',
     'k bro',
     'wn fo',
     'xes j',
     'umped',
     ' over',
     ' lazy',
     ' brow',
     'n, be']



### \A Matches beginning of string.


```python
re.findall('\AA', text)
```




    ['A']



### \Z Matches end of string. If a newline exists, it matches just before newline.


```python
re.findall('bears.\Z', text)
```




    ['bears.']



### \b Matches end of string.


```python
re.findall('\b[foxes]', text)
```




    []



### \n, \t, etc. Matches newlines, carriage returns, tabs, etc.


```python
re.findall('\n', text)
```




    []



### [Pp]ython Match "Python" or "python"


```python
re.findall('[Ff]oxes', 'foxes Foxes Doxes')
```




    ['foxes', 'Foxes']



### [0-9] Match any digit; same as [0123456789]


```python
re.findall('[Ff]oxes', 'foxes Foxes Doxes')
```




    ['foxes', 'Foxes']



### [a-z] Match any lowercase ASCII letter


```python
re.findall('[a-z]', 'foxes Foxes')
```




    ['f', 'o', 'x', 'e', 's', 'o', 'x', 'e', 's']



### [A-Z] Match any uppercase ASCII letter


```python
re.findall('[A-Z]', 'foxes Foxes')
```




    ['F']



### [a-zA-Z0-9] Match any of the above


```python
re.findall('[a-zA-Z0-9]', 'foxes Foxes')
```




    ['f', 'o', 'x', 'e', 's', 'F', 'o', 'x', 'e', 's']



### [^aeiou] Match anything other than a lowercase vowel


```python
re.findall('[^aeiou]', 'foxes Foxes')
```




    ['f', 'x', 's', ' ', 'F', 'x', 's']



### [^0-9] Match anything other than a digit


```python
re.findall('[^0-9]', 'foxes Foxes')
```




    ['f', 'o', 'x', 'e', 's', ' ', 'F', 'o', 'x', 'e', 's']



### ruby? Match "rub" or "ruby": the y is optional


```python
re.findall('foxes?', 'foxes Foxes')
```




    ['foxes']



### ruby* Match "rub" plus 0 or more ys


```python
re.findall('ox*', 'foxes Foxes')
```




    ['ox', 'ox']



### ruby+ Match "rub" plus 1 or more ys


```python
re.findall('ox+', 'foxes Foxes')
```




    ['ox', 'ox']



### \d{3} Match exactly 3 digits


```python
re.findall('\d{3}', text)
```




    ['120']



### \d{3,} Match 3 or more digits


```python
re.findall('\d{2,}', text)
```




    ['120', '30']



### \d{3,5} Match 3, 4, or 5 digits


```python
re.findall('\d{2,3}', text)
```




    ['120', '30']



### ^Python Match "Python" at the start of a string or internal line


```python
re.findall('^A', text)
```




    ['A']



### Python$ Match "Python" at the end of a string or line


```python
re.findall('bears.$', text)
```




    ['bears.']



### \APython Match "Python" at the start of a string


```python
re.findall('\AA', text)
```




    ['A']



### Python\Z Match "Python" at the end of a string


```python
re.findall('bears.\Z', text)
```




    ['bears.']



### Python(?=!) Match "Python", if followed by an exclamation point


```python
re.findall('bears(?=.)', text)
```




    ['bears']



### Python(?!!) Match "Python", if not followed by an exclamation point


```python
re.findall('foxes(?!!)', 'foxes foxes!')
```




    ['foxes']



### python|perl Match "python" or "perl"


```python
re.findall('foxes|foxes!', 'foxes foxes!')
```




    ['foxes', 'foxes']



### rub(y|le)) Match "ruby" or "ruble"


```python
re.findall('fox(es!)', 'foxes foxes!')
```




    ['es!']



### Python(!+|\?) "Python" followed by one or more ! or one ?


```python
re.findall('foxes(!)', 'foxes foxes!')
```




    ['!']


