Title: Copy Data From One Table To Another  
Slug: copy_data_between_tables  
Summary: Copy Data From One Table To Another in SQL.    
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

## Create Table


```python
%%sql

-- Create a table of criminals_1
CREATE TABLE criminals_1 (pid, name, age, sex, city, minor);
INSERT INTO criminals_1 VALUES (412, 'James Smith', 15, 'M', 'Santa Rosa', 1);
INSERT INTO criminals_1 VALUES (234, 'Bill James', 22, 'M', 'Santa Rosa', 0);
INSERT INTO criminals_1 VALUES (632, 'Stacy Miller', 23, 'F', 'Santa Rosa', 0);
INSERT INTO criminals_1 VALUES (621, 'Betty Bob', NULL, 'F', 'Petaluma', 1);
INSERT INTO criminals_1 VALUES (162, 'Jaden Ado', 49, 'M', NULL, 0);
INSERT INTO criminals_1 VALUES (901, 'Gordon Ado', 32, 'F', 'Santa Rosa', 0);
INSERT INTO criminals_1 VALUES (512, 'Bill Byson', 21, 'M', 'Santa Rosa', 0);
INSERT INTO criminals_1 VALUES (411, 'Bob Iton', NULL, 'M', 'San Francisco', 0);
```




    []



## View Table


```python
%%sql

-- Select all
SELECT *

-- From the table 'criminals_1'
FROM criminals_1
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
        <td>Bill James</td>
        <td>22</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>632</td>
        <td>Stacy Miller</td>
        <td>23</td>
        <td>F</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>621</td>
        <td>Betty Bob</td>
        <td>None</td>
        <td>F</td>
        <td>Petaluma</td>
        <td>1</td>
    </tr>
    <tr>
        <td>162</td>
        <td>Jaden Ado</td>
        <td>49</td>
        <td>M</td>
        <td>None</td>
        <td>0</td>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>512</td>
        <td>Bill Byson</td>
        <td>21</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>411</td>
        <td>Bob Iton</td>
        <td>None</td>
        <td>M</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
</table>



## Create New Empty Table


```python
%%sql

-- Create a table called criminals_2
CREATE TABLE criminals_2 (pid, name, age, sex, city, minor);
```




    []



## Copy Contents Of First Table Into Empty Table


```python
%%sql

-- Insert into the empty table
INSERT INTO criminals_2

-- Everything
SELECT * 

-- From the first table
FROM criminals_1;
```




    []



## View Previously Empty Table


```python
%%sql

-- Select everything
SELECT *

-- From the previously empty table
FROM criminals_2
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
        <td>Bill James</td>
        <td>22</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>632</td>
        <td>Stacy Miller</td>
        <td>23</td>
        <td>F</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>621</td>
        <td>Betty Bob</td>
        <td>None</td>
        <td>F</td>
        <td>Petaluma</td>
        <td>1</td>
    </tr>
    <tr>
        <td>162</td>
        <td>Jaden Ado</td>
        <td>49</td>
        <td>M</td>
        <td>None</td>
        <td>0</td>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>512</td>
        <td>Bill Byson</td>
        <td>21</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>0</td>
    </tr>
    <tr>
        <td>411</td>
        <td>Bob Iton</td>
        <td>None</td>
        <td>M</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
</table>


