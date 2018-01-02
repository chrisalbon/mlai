Title: Pie Chart In MatPlotLib  
Slug: matplotlib_pie_chart  
Summary: Pie Chart In MatPlotLib  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Visualization  
Authors: Chris Albon  

Based on: [Sebastian Raschka](http://nbviewer.ipython.org/github/rasbt/matplotlib-gallery/blob/master/ipynb/barplots.ipynb).

## Preliminaries


```python
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
```

## Create dataframe


```python
raw_data = {'officer_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'jan_arrests': [4, 24, 31, 2, 3],
        'feb_arrests': [25, 94, 57, 62, 70],
        'march_arrests': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['officer_name', 'jan_arrests', 'feb_arrests', 'march_arrests'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>officer_name</th>
      <th>jan_arrests</th>
      <th>feb_arrests</th>
      <th>march_arrests</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>4</td>
      <td>25</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>24</td>
      <td>94</td>
      <td>43</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>31</td>
      <td>57</td>
      <td>23</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>2</td>
      <td>62</td>
      <td>23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>3</td>
      <td>70</td>
      <td>51</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a column with the total arrests for each officer
df['total_arrests'] = df['jan_arrests'] + df['feb_arrests'] + df['march_arrests']
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>officer_name</th>
      <th>jan_arrests</th>
      <th>feb_arrests</th>
      <th>march_arrests</th>
      <th>total_arrests</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>4</td>
      <td>25</td>
      <td>5</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>24</td>
      <td>94</td>
      <td>43</td>
      <td>161</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>31</td>
      <td>57</td>
      <td>23</td>
      <td>111</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>2</td>
      <td>62</td>
      <td>23</td>
      <td>87</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>3</td>
      <td>70</td>
      <td>51</td>
      <td>124</td>
    </tr>
  </tbody>
</table>
</div>



## Make plot


```python
# Create a list of colors (from iWantHue)
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]

# Create a pie chart
plt.pie(
    # using data total)arrests
    df['total_arrests'],
    # with the labels being officer names
    labels=df['officer_name'],
    # with no shadows
    shadow=False,
    # with colors
    colors=colors,
    # with one slide exploded out
    explode=(0, 0, 0, 0, 0.15),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%',
    )

# View the plot drop above
plt.axis('equal')

# View the plot
plt.tight_layout()
plt.show()
```


![png](matplotlib_pie_chart_files/matplotlib_pie_chart_7_0.png)

