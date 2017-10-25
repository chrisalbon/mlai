Title: String Operations  
Slug: string_operations  
Summary: String Operations  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

**Python 3 has three string types**

- str() is for unicode
- bytes() is for binary data
- bytesarray() mutable variable of bytes

### Create some simulated text.


```python
string = 'The quick brown fox jumped over the lazy brown bear.'
```

### Capitalize the first letter.


```python
string_capitalized = string.capitalize()
string_capitalized
```




    'The quick brown fox jumped over the lazy brown bear.'



### Center the string with periods on either side, for a total of 79 characters


```python
string_centered = string.center(79, '.')
string_centered
```




    '..............The quick brown fox jumped over the lazy brown bear..............'



### Count the number of e's between the fifth and last character


```python
string_counted = string.count('e', 4, len(string))
string_counted
```




    4



### Locate any e's between the fifth and last character


```python
string_find = string.find('e', 4, len(string))
string_find
```




    24



### Are all characters are alphabet?


```python
string_isalpha = string.isalpha()
string_isalpha
```




    False



### Are all characters digits?


```python
string_isdigit = string.isdigit()
string_isdigit
```




    False



### Are all characters lower case?


```python
string_islower = string.islower()
string_islower
```




    False



### Are all chracters alphanumeric?


```python
string_isalnum = string.isalnum()
string_isalnum
```




    False



### Are all characters whitespaces?


```python
string_isalnum = string.isspace()
string_isalnum
```




    False



### Is the string properly titlespaced?


```python
string_istitle = string.istitle()
string_istitle
```




    False



### Are all the characters uppercase?


```python
string_isupper = string.isupper()
string_isupper
```




    False



### Return the lengths of string


```python
len(string)
```




    52



### Convert string to lower case


```python
string_lower = string.lower()
string_lower
```




    'the quick brown fox jumped over the lazy brown bear.'



### Convert string to lower case


```python
string_upper = string.upper()
string_upper
```




    'THE QUICK BROWN FOX JUMPED OVER THE LAZY BROWN BEAR.'



### Convert string to title case


```python
string_title = string.title()
string_title
```




    'The Quick Brown Fox Jumped Over The Lazy Brown Bear.'



### Convert string the inverted case


```python
string_swapcase = string.swapcase()
string_swapcase
```




    'tHE QUICK BROWN FOX JUMPED OVER THE LAZY BROWN BEAR.'



### Remove all leading whitespaces (i.e. to the left)


```python
string_lstrip = string.lstrip()
string_lstrip
```




    'The quick brown fox jumped over the lazy brown bear.'



### Remove all leading and trailing whitespaces (i.e. to the left and right)


```python
string_strip = string.strip()
string_strip
```




    'The quick brown fox jumped over the lazy brown bear.'



### Remove all trailing whitespaces (i.e. to the right)


```python
string_rstrip = string.rstrip()
string_rstrip
```




    'The quick brown fox jumped over the lazy brown bear.'



### Replace lower case e's with upper case E's, to a maximum of 4


```python
string_replace = string.replace('e', 'E', 4)
string_replace
```




    'ThE quick brown fox jumpEd ovEr thE lazy brown bear.'


