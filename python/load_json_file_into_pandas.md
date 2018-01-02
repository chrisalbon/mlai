Title: Load A JSON File Into Pandas  
Slug: load_json_file_into_pandas  
Summary: How to quickly load a JSON file into pandas.   
Date: 2016-08-31 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon 

## Preliminaries


```python
# Load library
import pandas as pd
```

## Load JSON File


```python
# Create URL to JSON file (alternatively this can be a filepath)
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json'

# Load the first sheet of the JSON file into a data frame
df = pd.read_json(url, orient='columns')

# View the first ten rows
df.head(10)
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
      <th>category</th>
      <th>datetime</th>
      <th>integer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2015-01-01 00:00:00</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>2015-01-01 00:00:01</td>
      <td>5</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0</td>
      <td>2015-01-01 00:00:10</td>
      <td>5</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>2015-01-01 00:00:11</td>
      <td>5</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>2015-01-01 00:00:12</td>
      <td>8</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0</td>
      <td>2015-01-01 00:00:13</td>
      <td>9</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0</td>
      <td>2015-01-01 00:00:14</td>
      <td>8</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0</td>
      <td>2015-01-01 00:00:15</td>
      <td>8</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0</td>
      <td>2015-01-01 00:00:16</td>
      <td>2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0</td>
      <td>2015-01-01 00:00:17</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>


