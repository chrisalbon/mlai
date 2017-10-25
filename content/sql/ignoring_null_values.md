Title: Ignoring Null or Missing Values   
Slug: ignoring_null_values   
Summary: Ignoring Null or Missing Values in SQL. 
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
INSERT INTO criminals VALUES (234, NULL, 22, 'M', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (632, NULL, 23, 'F', 'San Francisco', 0);
INSERT INTO criminals VALUES (901, 'Gordon Ado', 32, 'F', 'San Francisco', 0);
INSERT INTO criminals VALUES (512, 'Bill Byson', 21, 'M', 'Petaluma', 0);
```




    []



## Select Name And Ages Only When The Name Is Known


```python
%%sql

--  Select name and average age,
SELECT name, age

--  from the table 'criminals',
FROM criminals

-- if age is not a null value
WHERE name IS NOT NULL
```




<table>
    <tr>
        <th>name</th>
        <th>age</th>
    </tr>
    <tr>
        <td>James Smith</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Gordon Ado</td>
        <td>32</td>
    </tr>
    <tr>
        <td>Bill Byson</td>
        <td>21</td>
    </tr>
</table>


