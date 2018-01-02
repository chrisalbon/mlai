Title: Create Data Type And Value Rules
Slug: create_rules_constraining_data  
Summary: Create Data Type And Value Rules in SQL. 
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

## Create New Table With Constraints On What Data Can Be Inserted


```python
%%sql

-- Create a table of criminals
CREATE TABLE criminals 

(

-- With a prisoner ID (pid) that is a primary key and cannot be null
 pid    INT PRIMARY KEY     NOT NULL, 
 
-- With a name variable whose default value is John Doe
 name   TEXT                DEFAULT 'John Doe',
 
-- With an age variable that is an integer and has to be between 0 and 100
 age    INT                 CHECK(0 < age < 100)

);

```




    []



## Add Data To Table


```python
%%sql

INSERT INTO criminals VALUES (412, 'James Smith', 15);
INSERT INTO criminals VALUES (234, 'Bill James', 22);
INSERT INTO criminals VALUES (632, 'Bill Steve', 23);
INSERT INTO criminals VALUES (621, 'Betty Bob', NULL);
INSERT INTO criminals VALUES (162, 'Jaden Ado', 49);
INSERT INTO criminals VALUES (901, 'Gordon Ado', 32);
INSERT INTO criminals VALUES (512, 'Bill Byson', 21);
INSERT INTO criminals VALUES (411, 'Bob Iton', NULL);
```




    []



## View Table


```python
%%sql

SELECT *

FROM criminals
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
    </tr>
    <tr>
        <td>412</td>
        <td>James Smith</td>
        <td>15</td>
    </tr>
    <tr>
        <td>234</td>
        <td>Bill James</td>
        <td>22</td>
    </tr>
    <tr>
        <td>632</td>
        <td>Bill Steve</td>
        <td>23</td>
    </tr>
    <tr>
        <td>621</td>
        <td>Betty Bob</td>
        <td>None</td>
    </tr>
    <tr>
        <td>162</td>
        <td>Jaden Ado</td>
        <td>49</td>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
    </tr>
    <tr>
        <td>512</td>
        <td>Bill Byson</td>
        <td>21</td>
    </tr>
    <tr>
        <td>411</td>
        <td>Bob Iton</td>
        <td>None</td>
    </tr>
</table>


