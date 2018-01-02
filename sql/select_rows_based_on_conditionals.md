Title: Selecting Rows Based On Conditionals    
Slug: select_rows_based_on_conditionals    
Summary: Selecting Rows Based On Conditionals in SQL.    
Date: 2017-01-16 12:00    
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

## Create Data


```python
%%sql

-- Create a table of criminals
CREATE TABLE criminals (pid, name, age, sex, city, minor);
INSERT INTO criminals VALUES (412, 'James Smith', 15, 'M', 'Santa Rosa', 1);
INSERT INTO criminals VALUES (234, 'Bill Bayes', 22, 'M', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (632, 'Jack Killer', 23, 'F', 'San Francisco', 0);
INSERT INTO criminals VALUES (901, 'Gordon Ado', 32, 'F', 'San Francisco', 0);
INSERT INTO criminals VALUES (512, 'Bill Byson', 21, 'M', 'Petaluma', 0);
```




    []



## View All Rows


```python
%%sql

--  Select all
SELECT *

-- From the criminals table
FROM criminals
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>412</td>
        <td>James Smith</td>
        <td>15</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>1</td>
    </tr>
    <tr>
        <td>234</td>
        <td>Bill Bayes</td>
        <td>22</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>632</td>
        <td>Jack Killer</td>
        <td>23</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
    <tr>
        <td>512</td>
        <td>Bill Byson</td>
        <td>21</td>
        <td>M</td>
        <td>Petaluma</td>
        <td>0</td>
    </tr>
</table>



## View Rows Where Age Is Greater Than 30


```python
%%sql

--  Select all
SELECT distinct *

-- From the criminals table
FROM criminals

-- Where age is greater than 30
WHERE age > 30
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
</table>



## View Rows Where Age Is Greater Than Or Equal To 23


```python
%%sql

--  Select all
SELECT distinct *

-- From the criminals table
FROM criminals

-- Where age is greater than 23
WHERE age >= 23
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>632</td>
        <td>Jack Killer</td>
        <td>23</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
</table>



## View Rows Where Age Is 23


```python
%%sql

--  Select all
SELECT distinct *

-- From the criminals table
FROM criminals

-- Where age is greater than 23
WHERE age = 23
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>632</td>
        <td>Jack Killer</td>
        <td>23</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
</table>



## View Rows Where Age Is Not 23


```python
%%sql

--  Select all
SELECT distinct *

-- From the criminals table
FROM criminals

-- Where age is greater than 23
WHERE age <> 23
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>412</td>
        <td>James Smith</td>
        <td>15</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>1</td>
    </tr>
    <tr>
        <td>234</td>
        <td>Bill Bayes</td>
        <td>22</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
    <tr>
        <td>512</td>
        <td>Bill Byson</td>
        <td>21</td>
        <td>M</td>
        <td>Petaluma</td>
        <td>0</td>
    </tr>
</table>



## View Rows Where Name Begins With 'J'


```python
%%sql

--  Select all
SELECT distinct *

-- From the criminals table
FROM criminals

-- Where name starts with 'J'
WHERE name LIKE 'J%'
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>412</td>
        <td>James Smith</td>
        <td>15</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>1</td>
    </tr>
    <tr>
        <td>632</td>
        <td>Jack Killer</td>
        <td>23</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
</table>



## View Rows Where Name Contains The String 'ames'


```python
%%sql

--  Select all
SELECT distinct *

-- From the criminals table
FROM criminals

-- Where name contains the string 'ames'
WHERE name LIKE '%ames%'
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>412</td>
        <td>James Smith</td>
        <td>15</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>1</td>
    </tr>
</table>


