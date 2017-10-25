Title: Parse HTML  
Slug: parse_html  
Summary: How to parse HTML for machine learning in Python.   
Date: 2016-09-07 12:00  
Category: Machine Learning  
Tags: Preprocessing Text
Authors: Chris Albon

## Preliminaries


```python
# Load library
from bs4 import BeautifulSoup
```

## Create HTML


```python
# Create some HTML code
html = "<div class='full_name'><span style='font-weight:bold'>Masego</span> Azra</div>"
```

## Parse HTML


```python
# Parse html
soup = BeautifulSoup(html, "lxml")

# Find the div with the class "full_name", show text
soup.find("div", { "class" : "full_name" }).text
```




    'Masego Azra'


