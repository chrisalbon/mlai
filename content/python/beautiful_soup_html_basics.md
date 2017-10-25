Title: Beautiful Soup Basic HTML Scraping  
Slug: beautiful_soup_html_basics  
Summary: Beautiful Soup Basic HTML Scraping  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Web Scraping    
Authors: Chris Albon  

### Import the modules


```python
# Import required modules
import requests
from bs4 import BeautifulSoup
```

### Scrap the html and turn into a beautiful soup object


```python
# Create a variable with the url
url = 'http://chrisralbon.com'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'lxml')
```

### Select the website's title


```python
# View the title tag of the soup object
soup.title
```




    <title>Chris Albon</title>



### Website title tag's string


```python
# View the string within the title tag
soup.title.string
```




    'Chris Albon'



### First paragraph tag


```python
# view the paragraph tag of the soup
soup.p
```




    <p>I am a <a href="./pages/about.html">data scientist originally trained as a quantitative political scientist</a>. I specialize in the technical and organizational aspects of applying data science to political and social issues. </p>



### The parent of the title tag


```python
soup.title.parent.name
```




    'head'



### The first link tag


```python
soup.a
```




    <a class="navbar-brand" href=".">Chris Albon</a>



### Find all the link tags and list the first five


```python
soup.find_all('a')[0:5]
```




    [<a class="navbar-brand" href=".">Chris Albon</a>,
     <a aria-expanded="false" aria-haspopup="true" class="dropdown-toggle" data-toggle="dropdown" href="#" role="button">About<span class="caret"></span></a>,
     <a href="./pages/about.html">About Chris</a>,
     <a href="https://github.com/chrisalbon">GitHub</a>,
     <a href="https://twitter.com/chrisalbon">Twitter</a>]



### The string inside the first paragraph tag


```python
soup.p.string
```

### Find all the h2 tags and list the first five


```python
soup.find_all('h2')[0:5]
```




    [<h2 class="homepage_category_title">Articles</h2>,
     <h2 class="homepage_category_title">Projects</h2>,
     <h2 class="homepage_category_title">Python</h2>,
     <h2 class="homepage_category_title">R Stats</h2>,
     <h2 class="homepage_category_title">Regex</h2>]



### Find all the links on the page and list the first five


```python
soup.find_all('a')[0:5]
```




    [<a class="navbar-brand" href=".">Chris Albon</a>,
     <a aria-expanded="false" aria-haspopup="true" class="dropdown-toggle" data-toggle="dropdown" href="#" role="button">About<span class="caret"></span></a>,
     <a href="./pages/about.html">About Chris</a>,
     <a href="https://github.com/chrisalbon">GitHub</a>,
     <a href="https://twitter.com/chrisalbon">Twitter</a>]


