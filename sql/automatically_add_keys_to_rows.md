Title: Automatically Add Keys To Rows  
Slug: automatically_add_keys_to_rows  
Summary: Automatically Add Keys To Rows in SQL.   
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

## Create Data With 'pid' As An Auto-Generated Primary Key


```python
%%sql

-- Create a table of criminals with pid being a primary key integer that is auto-incremented
CREATE TABLE criminals (pid INTEGER PRIMARY KEY AUTOINCREMENT,
                        name, 
                        age, 
                        sex, 
                        city, 
                        minor);

-- Add a single row with a null value for pid
INSERT INTO criminals VALUES (NULL, 'James Smith', 15, 'M', 'Santa Rosa', 1);
```




    []



## View Table


```python
%%sql

-- Select everything
SELECT *

-- From the table 'criminals'
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
        <td>1</td>
        <td>James Smith</td>
        <td>15</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>1</td>
    </tr>
</table>



## Added More Rows With NULL Values For pid


```python
%%sql

INSERT INTO criminals VALUES (NULL, 'Bill James', 22, 'M', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (NULL, 'Stacy Miller', 23, 'F', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (NULL, 'Betty Bob', NULL, 'F', 'Petaluma', 1);
INSERT INTO criminals VALUES (NULL, 'Jaden Ado', 49, 'M', NULL, 0);
INSERT INTO criminals VALUES (NULL, 'Gordon Ado', 32, 'F', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (NULL, 'Bill Byson', 21, 'M', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (NULL, 'Bob Iton', NULL, 'M', 'San Francisco', 0);
```




    []



## View Table


```python
%%sql

-- Select everything
SELECT *

-- From the table 'criminals'
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
        <td>1</td>
        <td>James Smith</td>
        <td>15</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Bill James</td>
        <td>22</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Stacy Miller</td>
        <td>23</td>
        <td>F</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Betty Bob</td>
        <td>None</td>
        <td>F</td>
        <td>Petaluma</td>
        <td>1</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Jaden Ado</td>
        <td>49</td>
        <td>M</td>
        <td>None</td>
        <td>0</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Bill Byson</td>
        <td>21</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Bob Iton</td>
        <td>None</td>
        <td>M</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
</table>


