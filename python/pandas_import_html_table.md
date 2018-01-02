Title: Importing an HTML table into pandas  
Slug: pandas_import_html_table  
Summary: Importing an HTML table into pandas  
Date: 2016-05-01 12:00  
Category: Data Wrangling  
Tags: Basics  
Authors: Chris Albon  


```python
# Import the required module
import pandas as pd
```


```python
# Create a variable with the url to the website contain the html table
url = "http://www.w3schools.com/html/html_tables.asp"
```


```python
# Read the html table into pandas
data = pd.read_html(url, header=0)
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-6-1bfd2d51c2cb> in <module>()
          1 # Read the html table into pandas
    ----> 2 data = pd.read_html(url, header=0)
    

    /Users/chrisralbon/anaconda/lib/python3.5/site-packages/pandas/io/html.py in read_html(io, match, flavor, header, index_col, skiprows, attrs, parse_dates, tupleize_cols, thousands, encoding)
        868     _validate_header_arg(header)
        869     return _parse(flavor, io, match, header, index_col, skiprows,
    --> 870                   parse_dates, tupleize_cols, thousands, attrs, encoding)
    

    /Users/chrisralbon/anaconda/lib/python3.5/site-packages/pandas/io/html.py in _parse(flavor, io, match, header, index_col, skiprows, parse_dates, tupleize_cols, thousands, attrs, encoding)
        720     retained = None
        721     for flav in flavor:
    --> 722         parser = _parser_dispatch(flav)
        723         p = parser(io, compiled_match, attrs, encoding)
        724 


    /Users/chrisralbon/anaconda/lib/python3.5/site-packages/pandas/io/html.py in _parser_dispatch(flavor)
        664     if flavor in ('bs4', 'html5lib'):
        665         if not _HAS_HTML5LIB:
    --> 666             raise ImportError("html5lib not found, please install it")
        667         if not _HAS_BS4:
        668             raise ImportError(


    ImportError: html5lib not found, please install it


The resulting data will be a list of dataframe objects


```python
# View the data
data
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-9a6a81bab7f3> in <module>()
          1 # View the data
    ----> 2 data
    

    NameError: name 'data' is not defined



```python
# Select the first (and in this case only) dataframe object
data[0]
```
