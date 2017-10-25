Title: Select An Entire Table  
Slug: select_entire_table  
Summary: Select an entire table in SQL. 
Date: 2016-05-01 12:00  
Category: SQL  
Tags: Basics  
Authors: Chris Albon  

Note: This tutorial was written using [Catherine Devlin's SQL in Jupyter Notebooks library](https://github.com/catherinedevlin/ipython-sql). If you have not using a Jupyter Notebook, you can ignore the two lines of code below and any line containing `%%sql`. Furthermore, this tutorial uses SQLite's flavor of SQL, your version might have some differences in syntax.


```python
# Ignore
%load_ext sql
%sql sqlite://
```




    'Connected: None@None'



## Create Data


```python
%%sql

/* Create A Table Of Criminals */
CREATE TABLE criminals (pid, name, age, sex, city, minor);
INSERT INTO criminals VALUES (412, 'James Smith', 15, 'M', 'Santa Rosa', 1);
INSERT INTO criminals VALUES (234, 'Bill James', 22, 'M', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (632, 'Stacy Miller', 23, 'F', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (621, 'Betty Bob', NULL, 'F', 'Petaluma', 1);
INSERT INTO criminals VALUES (162, 'Jaden Ado', 49, 'M', NULL, 0);
INSERT INTO criminals VALUES (901, 'Gordon Ado', 32, 'F', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (512, 'Bill Byson', 21, 'M', 'Santa Rosa', 0);
INSERT INTO criminals VALUES (411, 'Bob Iton', NULL, 'M', 'San Francisco', 0);

/* Create A Table Of Crimes */
CREATE TABLE crimes (cid, crime, city, pid_arrested, cash_stolen);
INSERT INTO crimes VALUES (1, 'fraud', 'Santa Rosa', 412, 40000);
INSERT INTO crimes VALUES (1, 'burglary', 'Petaluma', 234, 2000);
INSERT INTO crimes VALUES (1, 'burglary', 'Santa Rosa', 632, 2000);
INSERT INTO crimes VALUES (1, 'larcony', 'Petaluma', 621, 3500); 
INSERT INTO crimes VALUES (1, 'burglary', 'Santa Rosa', 162, 1000); 
INSERT INTO crimes VALUES (1, 'larcony', 'Petaluma', 901, 50000); 
INSERT INTO crimes VALUES (1, 'fraud', 'San Francisco', 412, 60000); 
INSERT INTO crimes VALUES (1, 'burglary', 'Santa Rosa', 512, 7000); 
INSERT INTO crimes VALUES (1, 'burglary', 'San Francisco', 411, 3000); 
INSERT INTO crimes VALUES (1, 'robbery', 'Santa Rosa', 632, 2500); 
INSERT INTO crimes VALUES (1, 'robbery', 'Santa Rosa', 512, 3000);
```

    Done.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    Done.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.





    []



## View Both Tables


```python
%%sql

-- Select everything
SELECT *

-- From the table 'criminals'
FROM criminals
```

    Done.





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




```python
%%sql

-- Select everything
SELECT *

-- From the table 'crimes'
FROM crimes
```

    Done.





<table>
    <tr>
        <th>cid</th>
        <th>crime</th>
        <th>city</th>
        <th>pid_arrested</th>
        <th>cash_stolen</th>
    </tr>
    <tr>
        <td>1</td>
        <td>fraud</td>
        <td>Santa Rosa</td>
        <td>412</td>
        <td>40000</td>
    </tr>
    <tr>
        <td>1</td>
        <td>burglary</td>
        <td>Petaluma</td>
        <td>234</td>
        <td>2000</td>
    </tr>
    <tr>
        <td>1</td>
        <td>burglary</td>
        <td>Santa Rosa</td>
        <td>632</td>
        <td>2000</td>
    </tr>
    <tr>
        <td>1</td>
        <td>larcony</td>
        <td>Petaluma</td>
        <td>621</td>
        <td>3500</td>
    </tr>
    <tr>
        <td>1</td>
        <td>burglary</td>
        <td>Santa Rosa</td>
        <td>162</td>
        <td>1000</td>
    </tr>
    <tr>
        <td>1</td>
        <td>larcony</td>
        <td>Petaluma</td>
        <td>901</td>
        <td>50000</td>
    </tr>
    <tr>
        <td>1</td>
        <td>fraud</td>
        <td>San Francisco</td>
        <td>412</td>
        <td>60000</td>
    </tr>
    <tr>
        <td>1</td>
        <td>burglary</td>
        <td>Santa Rosa</td>
        <td>512</td>
        <td>7000</td>
    </tr>
    <tr>
        <td>1</td>
        <td>burglary</td>
        <td>San Francisco</td>
        <td>411</td>
        <td>3000</td>
    </tr>
    <tr>
        <td>1</td>
        <td>robbery</td>
        <td>Santa Rosa</td>
        <td>632</td>
        <td>2500</td>
    </tr>
    <tr>
        <td>1</td>
        <td>robbery</td>
        <td>Santa Rosa</td>
        <td>512</td>
        <td>3000</td>
    </tr>
</table>


