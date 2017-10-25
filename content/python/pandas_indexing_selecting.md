<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
Title: Indexing and Selecting Data With Pandas  
Slug: pandas_indexing_selecting  
Summary: Indexing and Selecting Data With Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# import the pandas module
import pandas as pd
```


```python
<<<<<<< Updated upstream
# Create an example dataframe about a fictional army
=======
# Create data
>>>>>>> Stashed changes
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35], 
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9], 
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

# Create data frame
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'deaths', 'battles', 'size', 'veterans', 'readiness', 'armored', 'deserters', 'origin'])

# Set index
df = df.set_index('origin')

# View first few rows
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>deaths</th>
      <th>battles</th>
      <th>size</th>
      <th>veterans</th>
      <th>readiness</th>
      <th>armored</th>
      <th>deserters</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>523</td>
      <td>5</td>
      <td>1045</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>California</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>52</td>
      <td>42</td>
      <td>957</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>25</td>
      <td>2</td>
      <td>1099</td>
      <td>62</td>
      <td>3</td>
      <td>1</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>616</td>
      <td>2</td>
      <td>1400</td>
      <td>26</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Maine</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>43</td>
      <td>4</td>
      <td>1592</td>
      <td>73</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### Select a column


```python
df['size']
```




    origin
    Arizona       1045
    California     957
    Texas         1099
    Florida       1400
    Maine         1592
    Iowa          1006
    Alaska         987
    Washington     849
    Oregon         973
    Wyoming       1005
    Louisana      1099
    Georgia       1523
    Name: size, dtype: int64



### Select multiple columns


```python
df[['size', 'veterans']]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>size</th>
      <th>veterans</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>1045</td>
      <td>1</td>
    </tr>
    <tr>
      <th>California</th>
      <td>957</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>1099</td>
      <td>62</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>1400</td>
      <td>26</td>
    </tr>
    <tr>
      <th>Maine</th>
      <td>1592</td>
      <td>73</td>
    </tr>
    <tr>
      <th>Iowa</th>
      <td>1006</td>
      <td>37</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>987</td>
      <td>949</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>849</td>
      <td>48</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>973</td>
      <td>48</td>
    </tr>
    <tr>
      <th>Wyoming</th>
      <td>1005</td>
      <td>435</td>
    </tr>
    <tr>
      <th>Louisana</th>
      <td>1099</td>
      <td>63</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1523</td>
      <td>345</td>
    </tr>
  </tbody>
</table>
</div>



### Select all rows by index label


```python
# Select all rows with the index label "Arizona"
df.loc[:'Arizona']
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>deaths</th>
      <th>battles</th>
      <th>size</th>
      <th>veterans</th>
      <th>readiness</th>
      <th>armored</th>
      <th>deserters</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>523</td>
      <td>5</td>
      <td>1045</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### Select rows by row number


```python
# Select every row up to 3
df.iloc[:2]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>deaths</th>
      <th>battles</th>
      <th>size</th>
      <th>veterans</th>
      <th>readiness</th>
      <th>armored</th>
      <th>deserters</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>523</td>
      <td>5</td>
      <td>1045</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>California</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>52</td>
      <td>42</td>
      <td>957</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select the second and third row
df.iloc[1:3]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>deaths</th>
      <th>battles</th>
      <th>size</th>
      <th>veterans</th>
      <th>readiness</th>
      <th>armored</th>
      <th>deserters</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>52</td>
      <td>42</td>
      <td>957</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>24</td>
<<<<<<< Updated upstream
=======
    </tr>
    <tr>
      <th>Texas</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>25</td>
      <td>2</td>
      <td>1099</td>
      <td>62</td>
      <td>3</td>
      <td>1</td>
      <td>31</td>
>>>>>>> Stashed changes
    </tr>
  </tbody>
</table>
</div>




```python
# Select every row beginning with the third row
df.iloc[2:]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>deaths</th>
      <th>battles</th>
      <th>size</th>
      <th>veterans</th>
      <th>readiness</th>
      <th>armored</th>
      <th>deserters</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Texas</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>25</td>
      <td>2</td>
      <td>1099</td>
      <td>62</td>
      <td>3</td>
      <td>1</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>616</td>
      <td>2</td>
      <td>1400</td>
      <td>26</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Maine</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>43</td>
      <td>4</td>
      <td>1592</td>
      <td>73</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Iowa</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>234</td>
      <td>7</td>
      <td>1006</td>
      <td>37</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>523</td>
      <td>8</td>
      <td>987</td>
      <td>949</td>
      <td>2</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>62</td>
      <td>3</td>
      <td>849</td>
      <td>48</td>
      <td>3</td>
      <td>1</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>62</td>
      <td>4</td>
      <td>973</td>
      <td>48</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Wyoming</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>73</td>
      <td>7</td>
      <td>1005</td>
      <td>435</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Louisana</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>37</td>
      <td>8</td>
      <td>1099</td>
      <td>63</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>35</td>
      <td>9</td>
      <td>1523</td>
      <td>345</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### Select columns by column position


```python
# Select the first 2 columns
df.iloc[:,:2]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>Nighthawks</td>
      <td>1st</td>
    </tr>
    <tr>
      <th>California</th>
      <td>Nighthawks</td>
      <td>1st</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>Nighthawks</td>
      <td>2nd</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>Nighthawks</td>
      <td>2nd</td>
    </tr>
    <tr>
      <th>Maine</th>
      <td>Dragoons</td>
      <td>1st</td>
    </tr>
    <tr>
      <th>Iowa</th>
      <td>Dragoons</td>
      <td>1st</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>Dragoons</td>
      <td>2nd</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>Dragoons</td>
      <td>2nd</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>Scouts</td>
      <td>1st</td>
    </tr>
    <tr>
      <th>Wyoming</th>
      <td>Scouts</td>
      <td>1st</td>
    </tr>
    <tr>
      <th>Louisana</th>
      <td>Scouts</td>
      <td>2nd</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>Scouts</td>
      <td>2nd</td>
    </tr>
  </tbody>
</table>
</div>



### Select by conditionals (boolean)


```python
# Select rows where df.deaths is greater than 50
df[df['deaths'] > 50]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>deaths</th>
      <th>battles</th>
      <th>size</th>
      <th>veterans</th>
      <th>readiness</th>
      <th>armored</th>
      <th>deserters</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>523</td>
      <td>5</td>
      <td>1045</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>California</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>52</td>
      <td>42</td>
      <td>957</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>616</td>
      <td>2</td>
      <td>1400</td>
      <td>26</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Iowa</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>234</td>
      <td>7</td>
      <td>1006</td>
      <td>37</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>523</td>
      <td>8</td>
      <td>987</td>
      <td>949</td>
      <td>2</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>62</td>
      <td>3</td>
      <td>849</td>
      <td>48</td>
      <td>3</td>
      <td>1</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>62</td>
      <td>4</td>
      <td>973</td>
      <td>48</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Wyoming</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>73</td>
      <td>7</td>
      <td>1005</td>
      <td>435</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select rows where df.deaths is greater than 500 or less than 50
df[(df['deaths'] > 500) | (df['deaths'] < 50)]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>deaths</th>
      <th>battles</th>
      <th>size</th>
      <th>veterans</th>
      <th>readiness</th>
      <th>armored</th>
      <th>deserters</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>523</td>
      <td>5</td>
      <td>1045</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>25</td>
      <td>2</td>
      <td>1099</td>
      <td>62</td>
      <td>3</td>
      <td>1</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>616</td>
      <td>2</td>
      <td>1400</td>
      <td>26</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Maine</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>43</td>
      <td>4</td>
      <td>1592</td>
      <td>73</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>523</td>
      <td>8</td>
      <td>987</td>
      <td>949</td>
      <td>2</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Louisana</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>37</td>
      <td>8</td>
      <td>1099</td>
      <td>63</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>35</td>
      <td>9</td>
      <td>1523</td>
      <td>345</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select all the regiments not named "Dragoons"
df[~(df['regiment'] == 'Dragoons')]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>deaths</th>
      <th>battles</th>
      <th>size</th>
      <th>veterans</th>
      <th>readiness</th>
      <th>armored</th>
      <th>deserters</th>
    </tr>
    <tr>
      <th>origin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>523</td>
      <td>5</td>
      <td>1045</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>California</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>52</td>
      <td>42</td>
      <td>957</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>25</td>
      <td>2</td>
      <td>1099</td>
      <td>62</td>
      <td>3</td>
      <td>1</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>616</td>
      <td>2</td>
      <td>1400</td>
      <td>26</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>62</td>
      <td>4</td>
      <td>973</td>
      <td>48</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Wyoming</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>73</td>
      <td>7</td>
      <td>1005</td>
      <td>435</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Louisana</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>37</td>
      <td>8</td>
      <td>1099</td>
      <td>63</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>35</td>
      <td>9</td>
      <td>1523</td>
      <td>345</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>


