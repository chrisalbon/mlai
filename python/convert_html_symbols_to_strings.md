Title: Convert HTML Characters To Strings    
Slug: convert_html_symbols_to_strings  
Summary: Convert HTML Characters To Strings Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  


```python
## Preliminaries
```


```python
import html
```


```python
## Create Text
```


```python
text = 'This item costs &#165;400 or &#163;4.'
```


```python
## Convert To String
```


```python
html.unescape(text)
```




    'This item costs ¥400 or £4.'




```python
## Convert To HTML Entities
```


```python
html.escape(text)
```




    'This item costs &amp;#165;400 or &amp;#163;4.'


