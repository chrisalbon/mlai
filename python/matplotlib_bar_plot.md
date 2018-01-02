Title: Bar Plot In MatPlotLib  
Slug: matplotlib_bar_plot  
Summary: Bar Plot In MatPlotLib  
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
# Create a list of the mean scores for each variable
mean_values = [df['pre_score'].mean(), df['mid_score'].mean(), df['post_score'].mean()]

# Create a list of variances, which are set at .25 above and below the score
variance = [df['pre_score'].mean() * 0.25, df['pre_score'].mean() * 0.25, df['pre_score'].mean() * 0.25]

# Set the bar labels
bar_labels = ['Pre Score', 'Mid Score', 'Post Score']

# Create the x position of the bars
x_pos = list(range(len(bar_labels)))

# Create the plot bars
# In x position
plt.bar(x_pos,
        # using the data from the mean_values
        mean_values, 
        # with a y-error lines set at variance
        yerr=variance, 
        # aligned in the center
        align='center',
        # with color
        color='#FFC222',
        # alpha 0.5
        alpha=0.5)

# add a grid
plt.grid()

# set height of the y-axis
max_y = max(zip(mean_values, variance)) # returns a tuple, here: (3, 5)
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])

# set axes labels and title
plt.ylabel('Score')
plt.xticks(x_pos, bar_labels)
plt.title('Mean Scores For Each Test')

plt.show()
```


![png](matplotlib_bar_plot_files/matplotlib_bar_plot_6_0.png)

