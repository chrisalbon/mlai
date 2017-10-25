Title: Load Excel Spreadsheet As Pandas Dataframe  
Slug: pandas_dataframe_load_xls  
Summary: Load Excel Spreadsheet As Pandas Dataframe  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# import modules
import pandas as pd
```


```python
# Import the excel file and call it xls_file
xls_file = pd.ExcelFile('../data/example.xls')
xls_file
```




    <pandas.io.excel.ExcelFile at 0x111912be0>




```python
# View the excel file's sheet names
xls_file.sheet_names
```




    ['Sheet1']




```python
# Load the xls file's Sheet1 as a dataframe
df = xls_file.parse('Sheet1')
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>deaths_attacker</th>
      <th>deaths_defender</th>
      <th>soldiers_attacker</th>
      <th>soldiers_defender</th>
      <th>wounded_attacker</th>
      <th>wounded_defender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1945</td>
      <td>425</td>
      <td>423</td>
      <td>2532</td>
      <td>37235</td>
      <td>41</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1956</td>
      <td>242</td>
      <td>264</td>
      <td>6346</td>
      <td>2523</td>
      <td>214</td>
      <td>1424</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1964</td>
      <td>323</td>
      <td>1231</td>
      <td>3341</td>
      <td>2133</td>
      <td>131</td>
      <td>131</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1969</td>
      <td>223</td>
      <td>23</td>
      <td>6732</td>
      <td>1245</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1971</td>
      <td>783</td>
      <td>23</td>
      <td>12563</td>
      <td>2671</td>
      <td>123</td>
      <td>34</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1981</td>
      <td>436</td>
      <td>42</td>
      <td>2356</td>
      <td>7832</td>
      <td>124</td>
      <td>124</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1982</td>
      <td>324</td>
      <td>124</td>
      <td>253</td>
      <td>2622</td>
      <td>264</td>
      <td>1124</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1992</td>
      <td>3321</td>
      <td>631</td>
      <td>5277</td>
      <td>3331</td>
      <td>311</td>
      <td>1431</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1999</td>
      <td>262</td>
      <td>232</td>
      <td>2732</td>
      <td>2522</td>
      <td>132</td>
      <td>122</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2004</td>
      <td>843</td>
      <td>213</td>
      <td>6278</td>
      <td>26773</td>
      <td>623</td>
      <td>2563</td>
    </tr>
  </tbody>
</table>
</div>


