Title: Nested Select    
Slug: nested_select
Summary: Nested Select Based On Conditions in SQL. 
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



## Select Based On The Result Of A Select


```python
%%sql

--  Select name and age,
SELECT name, age

--  from the table 'criminals',
FROM criminals

--  where age is greater than,
WHERE age > 
     --  select age,
    (SELECT age
     --  from criminals
     FROM criminals
     --  where the name is 'James Smith'
     WHERE name == 'James Smith')
```




<table>
    <tr>
        <th>name</th>
        <th>age</th>
    </tr>
    <tr>
        <td>Bill James</td>
        <td>22</td>
    </tr>
    <tr>
        <td>Stacy Miller</td>
        <td>23</td>
    </tr>
    <tr>
        <td>Jaden Ado</td>
        <td>49</td>
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


