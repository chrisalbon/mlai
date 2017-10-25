Title: Dates And Times  
Slug: dates_and_times
Summary: Dates and times in SQL. 
Date: 2016-05-01 12:00  
Category: SQL  
Tags: Basics  
Authors: Chris Albon  

Note: This tutorial was written using [Catherine Devlin's SQL in Jupyter Notebooks library](https://github.com/catherinedevlin/ipython-sql). If you have not using a Jupyter Notebook, you can ignore the two lines of code below and any line containing `%%sql`. Furthermore, this tutorial uses SQLite's flavor of SQL, your version might have some differences in syntax.

For more, check out [Learning SQL](http://amzn.to/2jRriHj) by Alan Beaulieu.


```python
# Ignore
%load_ext sql
%sql sqlite://
%config SqlMagic.feedback = False
```

## Get Current Date


```python
%%sql

-- Select the current date
SELECT date('now');
```




<table>
    <tr>
        <th>date(&#x27;now&#x27;)</th>
    </tr>
    <tr>
        <td>2017-01-19</td>
    </tr>
</table>



## Get Current Date And Time


```python
%%sql

-- Select the unix time code '1200762133'
SELECT datetime('now', 'unixepoch');
```




<table>
    <tr>
        <th>datetime(&#x27;now&#x27;, &#x27;unixepoch&#x27;)</th>
    </tr>
    <tr>
        <td>1970-01-29 10:42:53</td>
    </tr>
</table>



## Compute A UNIX timestamp into a date and time


```python
%%sql

-- Select the unix time code '1169229733'
SELECT datetime(1169229733, 'unixepoch');
```




<table>
    <tr>
        <th>datetime(1169229733, &#x27;unixepoch&#x27;)</th>
    </tr>
    <tr>
        <td>2007-01-19 18:02:13</td>
    </tr>
</table>



## Compute A UNIX timestamp into a date and time and convert to the local timezone.


```python
%%sql

-- Select the unix time code '1171904533' and convert to the machine's local timezone
SELECT datetime(1171904533, 'unixepoch', 'localtime');
```




<table>
    <tr>
        <th>datetime(1171904533, &#x27;unixepoch&#x27;, &#x27;localtime&#x27;)</th>
    </tr>
    <tr>
        <td>2007-02-19 10:02:13</td>
    </tr>
</table>



## Compute The Day Of The Week


```python
%%sql

-- Select the the day of this week (0 = Sunday, 4 = Thursday)
SELECT strftime('%w','now');
```




<table>
    <tr>
        <th>strftime(&#x27;%w&#x27;,&#x27;now&#x27;)</th>
    </tr>
    <tr>
        <td>4</td>
    </tr>
</table>


