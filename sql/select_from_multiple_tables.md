Title: Select From Multiple Tables Simultaneously  
Slug: select_from_multiple_tables  
Summary: Merge tables in SQL. 
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

## Create Two Tables, Criminals And Crimes


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

-- Create a table of crimes
CREATE TABLE crimes (cid, crime, city, pid_arrested, cash_stolen);
INSERT INTO crimes VALUES (1, 'fraud', 'Santa Rosa', 412, 40000);
INSERT INTO crimes VALUES (2, 'burglary', 'Petaluma', 234, 2000);
INSERT INTO crimes VALUES (3, 'burglary', 'Santa Rosa', 632, 2000);
INSERT INTO crimes VALUES (4, NULL, NULL, 621, 3500); 
INSERT INTO crimes VALUES (5, 'burglary', 'Santa Rosa', 162, 1000); 
INSERT INTO crimes VALUES (6, NULL, 'Petaluma', 901, 50000); 
INSERT INTO crimes VALUES (7, 'fraud', 'San Francisco', 412, 60000); 
INSERT INTO crimes VALUES (8, 'burglary', 'Santa Rosa', 512, 7000); 
INSERT INTO crimes VALUES (9, 'burglary', 'San Francisco', 411, 3000); 
INSERT INTO crimes VALUES (10, 'robbery', 'Santa Rosa', 632, 2500); 
INSERT INTO crimes VALUES (11, 'robbery', 'Santa Rosa', 512, 3000);
```




    []



## View All Unique City Names From Both Tables


```python
%%sql

-- Select city name
SELECT city 

-- From criminals table
FROM criminals

-- Then combine with
UNION

-- Select city names
SELECT city 

-- From crimes table
FROM crimes;
```




<table>
    <tr>
        <th>city</th>
    </tr>
    <tr>
        <td>None</td>
    </tr>
    <tr>
        <td>Petaluma</td>
    </tr>
    <tr>
        <td>San Francisco</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
</table>



## View All City Names From Both Tables


```python
%%sql

-- Select city name
SELECT city 

-- From criminals table
FROM criminals

-- Then combine with
UNION ALL

-- Select city names
SELECT city 

-- From crimes table
FROM crimes;
```




<table>
    <tr>
        <th>city</th>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>Petaluma</td>
    </tr>
    <tr>
        <td>None</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>San Francisco</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>Petaluma</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>None</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>Petaluma</td>
    </tr>
    <tr>
        <td>San Francisco</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>San Francisco</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
    </tr>
</table>


