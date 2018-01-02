Title: Using Aliases    
Slug: aliases    
Summary: Using Aliases in SQL.    
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
INSERT INTO criminals VALUES (234, 'Bill James', 22, 'M', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (632, 'Stacy Miller', 23, 'F', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (621, 'Betty Bob', NULL, 'F', 'Petaluma', 1);
INSERT INTO criminals VALUES (162, 'Jaden Ado', 49, 'M', NULL, 0);
INSERT INTO criminals VALUES (901, 'Gordon Ado', 32, 'F', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (512, 'Bill Byson', 21, 'M', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (411, 'Bob Iton', NULL, 'M', 'San Francisco', 0);
```




    []



## Alias Criminals Table A `C`, Then Select All Names From `C`


```python
%%sql

--  Select all names from the table 'c'
SELECT c.name

-- From the criminals table, now called c
FROM criminals AS c
```




<table>
    <tr>
        <th>name</th>
    </tr>
    <tr>
        <td>James Smith</td>
    </tr>
    <tr>
        <td>Bill James</td>
    </tr>
    <tr>
        <td>Stacy Miller</td>
    </tr>
    <tr>
        <td>Betty Bob</td>
    </tr>
    <tr>
        <td>Jaden Ado</td>
    </tr>
    <tr>
        <td>Gordon Ado</td>
    </tr>
    <tr>
        <td>Bill Byson</td>
    </tr>
    <tr>
        <td>Bob Iton</td>
    </tr>
</table>


