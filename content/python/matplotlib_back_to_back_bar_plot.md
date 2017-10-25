Title: Back To Back Bar Plot In MatPlotLib  
Slug: matplotlib_back_to_back_bar_plot  
Summary: Back To Back Bar Plot In MatPlotLib  
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
import numpy as np
```

## Create dataframe


```python
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'pre_score': [4, 24, 31, 2, 3],
        'mid_score': [25, 94, 57, 62, 70],
        'post_score': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'pre_score', 'mid_score', 'post_score'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>pre_score</th>
      <th>mid_score</th>
      <th>post_score</th>
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



## Make plot


```python
# input data, specifically the second and 
# third rows, skipping the first column
x1 = df.ix[1, 1:]
x2 = df.ix[2, 1:]

# Create the bar labels
bar_labels = ['Pre Score', 'Mid Score', 'Post Score']

# Create a figure
fig = plt.figure(figsize=(8,6))

# Set the y position
y_pos = np.arange(len(x1))
y_pos = [x for x in y_pos]
plt.yticks(y_pos, bar_labels, fontsize=10)

# Create a horizontal bar in the position y_pos
plt.barh(y_pos, 
         # using x1 data
         x1, 
         # that is centered
         align='center', 
         # with alpha 0.4
         alpha=0.4, 
         # and color green
         color='#263F13')

# Create a horizontal bar in the position y_pos
plt.barh(y_pos, 
         # using NEGATIVE x2 data
         -x2,
         # that is centered
         align='center', 
         # with alpha 0.4
         alpha=0.4, 
         # and color green
         color='#77A61D')

# annotation and labels
plt.xlabel('Tina\'s Score: Light Green. Molly\'s Score: Dark Green')
t = plt.title('Comparison of Molly and Tina\'s Score')
plt.ylim([-1,len(x1)+0.1])
plt.xlim([-max(x2)-10, max(x1)+10])
plt.grid()

plt.show()
```


![png](matplotlib_back_to_back_bar_plot_files/matplotlib_back_to_back_bar_plot_6_0.png)

