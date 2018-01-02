Title: Calculate Counts, Sums, Max, and Averages    
Slug: sums_counts_max_averages    
Summary: Calculate Counts, Sums, and Averages in SQL. 
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
INSERT INTO criminals VALUES (632, 'Stacy Miller', 23, 'F', 'San Francisco', 0);
INSERT INTO criminals VALUES (901, 'Gordon Ado', 32, 'F', 'San Francisco', 0);
INSERT INTO criminals VALUES (512, 'Bill Byson', 21, 'M', 'Petaluma', 0);
```




    []



## View Average Ages By City


```python
%%sql

--  Select name and average age,
SELECT city, avg(age)

--  from the table 'criminals',
FROM criminals

-- after grouping by city
GROUP BY city
```




<table>
    <tr>
        <th>city</th>
        <th>avg(age)</th>
    </tr>
    <tr>
        <td>Petaluma</td>
        <td>21.0</td>
    </tr>
    <tr>
        <td>San Francisco</td>
        <td>27.5</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
        <td>18.5</td>
    </tr>
</table>



## View Max Age By City


```python
%%sql

--  Select name and average age,
SELECT city, max(age)

--  from the table 'criminals',
FROM criminals

-- after grouping by city
GROUP BY city
```




<table>
    <tr>
        <th>city</th>
        <th>max(age)</th>
    </tr>
    <tr>
        <td>Petaluma</td>
        <td>21</td>
    </tr>
    <tr>
        <td>San Francisco</td>
        <td>32</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
        <td>22</td>
    </tr>
</table>



## View Count Of Criminals By City


```python
%%sql

--  Select name and average age,
SELECT city, count(name)

--  from the table 'criminals',
FROM criminals

-- after grouping by city
GROUP BY city
```




<table>
    <tr>
        <th>city</th>
        <th>count(name)</th>
    </tr>
    <tr>
        <td>Petaluma</td>
        <td>1</td>
    </tr>
    <tr>
        <td>San Francisco</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
        <td>2</td>
    </tr>
</table>



## View Total Age By City


```python
%%sql

--  Select name and average age,
SELECT city, total(age)

--  from the table 'criminals',
FROM criminals

-- after grouping by city
GROUP BY city
```




<table>
    <tr>
        <th>city</th>
        <th>total(age)</th>
    </tr>
    <tr>
        <td>Petaluma</td>
        <td>21.0</td>
    </tr>
    <tr>
        <td>San Francisco</td>
        <td>55.0</td>
    </tr>
    <tr>
        <td>Santa Rosa</td>
        <td>37.0</td>
    </tr>
</table>


