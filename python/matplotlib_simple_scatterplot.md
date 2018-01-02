Title: Scatterplot In MatPlotLib  
Slug: matplotlib_simple_scatterplot  
Summary: Scatterplot In MatPlotLib  
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

# Set ipython's max row display
pd.set_option('display.max_row', 1000)

# Set iPython's max column width to 50
pd.set_option('display.max_columns', 50)
```

## Create dataframe


```python
df = pd.read_csv('https://raw.githubusercontent.com/chrisalbon/war_of_the_five_kings_dataset/master/5kings_battles_v1.csv')
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>year</th>
      <th>battle_number</th>
      <th>attacker_king</th>
      <th>defender_king</th>
      <th>attacker_1</th>
      <th>attacker_2</th>
      <th>attacker_3</th>
      <th>attacker_4</th>
      <th>defender_1</th>
      <th>defender_2</th>
      <th>defender_3</th>
      <th>defender_4</th>
      <th>attacker_outcome</th>
      <th>battle_type</th>
      <th>major_death</th>
      <th>major_capture</th>
      <th>attacker_size</th>
      <th>defender_size</th>
      <th>attacker_commander</th>
      <th>defender_commander</th>
      <th>summer</th>
      <th>location</th>
      <th>region</th>
      <th>note</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Battle of the Golden Tooth</td>
      <td>298</td>
      <td>1</td>
      <td>Joffrey/Tommen Baratheon</td>
      <td>Robb Stark</td>
      <td>Lannister</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Tully</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>win</td>
      <td>pitched battle</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>15000.0</td>
      <td>4000.0</td>
      <td>Jaime Lannister</td>
      <td>Clement Piper, Vance</td>
      <td>1.0</td>
      <td>Golden Tooth</td>
      <td>The Westerlands</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Battle at the Mummer's Ford</td>
      <td>298</td>
      <td>2</td>
      <td>Joffrey/Tommen Baratheon</td>
      <td>Robb Stark</td>
      <td>Lannister</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Baratheon</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>win</td>
      <td>ambush</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>120.0</td>
      <td>Gregor Clegane</td>
      <td>Beric Dondarrion</td>
      <td>1.0</td>
      <td>Mummer's Ford</td>
      <td>The Riverlands</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Battle of Riverrun</td>
      <td>298</td>
      <td>3</td>
      <td>Joffrey/Tommen Baratheon</td>
      <td>Robb Stark</td>
      <td>Lannister</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Tully</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>win</td>
      <td>pitched battle</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>15000.0</td>
      <td>10000.0</td>
      <td>Jaime Lannister, Andros Brax</td>
      <td>Edmure Tully, Tytos Blackwood</td>
      <td>1.0</td>
      <td>Riverrun</td>
      <td>The Riverlands</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Battle of the Green Fork</td>
      <td>298</td>
      <td>4</td>
      <td>Robb Stark</td>
      <td>Joffrey/Tommen Baratheon</td>
      <td>Stark</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Lannister</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>loss</td>
      <td>pitched battle</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>18000.0</td>
      <td>20000.0</td>
      <td>Roose Bolton, Wylis Manderly, Medger Cerwyn, H...</td>
      <td>Tywin Lannister, Gregor Clegane, Kevan Lannist...</td>
      <td>1.0</td>
      <td>Green Fork</td>
      <td>The Riverlands</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Battle of the Whispering Wood</td>
      <td>298</td>
      <td>5</td>
      <td>Robb Stark</td>
      <td>Joffrey/Tommen Baratheon</td>
      <td>Stark</td>
      <td>Tully</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Lannister</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>win</td>
      <td>ambush</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1875.0</td>
      <td>6000.0</td>
      <td>Robb Stark, Brynden Tully</td>
      <td>Jaime Lannister</td>
      <td>1.0</td>
      <td>Whispering Wood</td>
      <td>The Riverlands</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Make plot


```python
# Create a figure
plt.figure(figsize=(10,8))

# Create a scatterplot of,
            # attacker size in year 298 as the x axis
plt.scatter(df['attacker_size'][df['year'] == 298], 
            # attacker size in year 298 as the y axis
            df['defender_size'][df['year'] == 298], 
            # the marker as
            marker='x', 
            # the color
            color='b',
            # the alpha
            alpha=0.7,
            # with size
            s = 124,
            # labelled this
            label='Year 298')
            
            # attacker size in year 299 as the x axis
plt.scatter(df['attacker_size'][df['year'] == 299], 
            # defender size in year 299 as the y axis
            df['defender_size'][df['year'] == 299], 
            # the marker as
            marker='o', 
            # the color
            color='r', 
            # the alpha
            alpha=0.7,
            # with size
            s = 124,
            # labelled this
            label='Year 299')

            # attacker size in year 300 as the x axis
plt.scatter(df['attacker_size'][df['year'] == 300], 
            # defender size in year 300 as the y axis
            df['defender_size'][df['year'] == 300], 
            # the marker as
            marker='^', 
            # the color
            color='g', 
            # the alpha
            alpha=0.7, 
            # with size
            s = 124,
            # labelled this
            label='Year 300')

# Chart title
plt.title('Battles Of The War Of The Five Kings')

# y label
plt.ylabel('Defender Size')

# x label
plt.xlabel('Attacker Size')

# and a legend
plt.legend(loc='upper right')

# set the figure boundaries
plt.xlim([min(df['attacker_size'])-1000, max(df['attacker_size'])+1000])
plt.ylim([min(df['defender_size'])-1000, max(df['defender_size'])+1000])

plt.show()
```


![png](matplotlib_simple_scatterplot_files/matplotlib_simple_scatterplot_6_0.png)

