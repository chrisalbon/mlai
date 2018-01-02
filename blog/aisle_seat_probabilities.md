Title: What Is The Probability An Economy Class Seat Is An Aisle Seat?
Slug: aisle_seat_probabilities
Summary: What Is The Probability An Economy Class Seat Is An Aisle Seat?
Date: 2016-05-01 12:00
Category: Blog
Tags:
Authors: Chris Albon

There are two types of people in the world, aisle seaters and window seaters. I am an aisle seater, nothing is worse than limited bathroom access on a long flight. The first thing I do when I get my ticket is check to see if I have a window seat. If not, I immediately head over to the airline counter and try to get one.

Last flight, on Turkish Airlines, I ran into a curious situation. I recieved my boarding pass with my seat number, 18C, but the ticket did not specify if C was an aisle seat or not. Making matters worse, the airline counter was swamped with a few dozen people. So I asked myself: **given only the seat letter, C, what is the probability that it is an aisle seat?**

Later, on the flight, I decided to find out.

## Preliminaries


```python
# Import required modules
import pandas as pd
import numpy as np

# Set plots to display in the iPython notebook
%matplotlib inline
```

## Setup possible seat configurations

I am a pretty frequently flyer on a variety of airlines and aircraft. There are a variety of seating configurations out there, but typically they follow some basic rules:

- No window cluster of seats has more than three seats.
- On small flights with three seats, the single seat is on the left side.
- No flight has more than nine rows.

Based on these rules, here are the "typical" seating configurations from aircraft with between two and nine seats per row. A '1' codifies that a seat is an aisle seat, a '0' codifies that it is a non-aisle seat (i.e. window or middle), and 'np.nan' denotes that the aircraft has less than nine seats (this is so all the list lengths are the same). 


```python
# An aircraft with two seats per row
rows2 = [1,1, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]

# An aircraft with three seats per row
rows3 = [1,1,0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,]

# An aircraft with four seats per row
rows4 = [0,1,1,0, np.nan, np.nan, np.nan, np.nan, np.nan]

# An aircraft with five seats per row
rows5 = [0,1,1,0,0, np.nan, np.nan,np.nan, np.nan]

# An aircraft with six seats per row
rows6 = [0,1,1,1,1,0, np.nan, np.nan, np.nan]

# An aircraft with seven seats per row
rows7 = [0,1,1,0,1,1,0, np.nan, np.nan]

# An aircraft with eight seats per row
rows8 = [0,0,1,1,1,1,0,0, np.nan]

# An aircraft with nine seats per row
rows9 = [0,0,1,1,0,1,1,0,0]
```

For example, in an aircraft with five seats per row, `rows5`, the seating arrangement would be:

1. window
2. aisle
3. aisle
4. middle
5. window
6. no seat
7. no seat
8. no seat
9. no seat

Next, I'm take advantage of pandas row summation options, but to do this I need to wrangle the data into a pandas dataframe. Essentially I am using the pandas dataframe as a matrix.


```python
# Create a list variable of all possible aircraft configurations
seating_map = [rows2, rows3, rows4, rows5, rows6, rows7, rows8, rows9]
```


```python
# Create a dataframe from the seating_map variable
df = pd.DataFrame(seating_map, 
                  columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                  index=['rows2', 'rows3', 'rows4', 'rows5', 'rows6', 'rows7', 'rows8', 'rows9'])
```

Here is all the data we need to construct our probabilities. The columns represent individual seat letters (A, B, etc.) while the rows represent the number of seats-per-row in the aircraft.


```python
# View the dataframe
df
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
      <th>I</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rows2</th>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>rows3</th>
      <td>1</td>
      <td>1</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>rows4</th>
      <td>0</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>rows5</th>
      <td>0</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>rows6</th>
      <td>0</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>rows7</th>
      <td>0</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>rows8</th>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>rows9</th>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## Calculate aisle probability

Because each aircraft seats-per-row configuration (i.e. row) is binary (1 if aisle, 0 if non-aisle), the probability that a seat is an aisle is simply the mean value of each seat letter (i.e. column).


```python
# Create a list wherein each element is the mean value of a column
aisle_probability = [df['A'].mean(), 
                     df['B'].mean(),
                     df['C'].mean(),
                     df['D'].mean(),
                     df['E'].mean(),
                     df['F'].mean(),
                     df['G'].mean(),
                     df['H'].mean(),
                     df['I'].mean()]
```


```python
# Display the variable
aisle_probability
```




    [0.25, 0.75, 0.8571428571428571, 0.5, 0.6, 0.75, 0.3333333333333333, 0.0, 0.0]



So there you have it, the probability that each seat letter is an aisle. However, we can make the presentation a little more intituative.

## Visualize seat letter probabilities

The most obvious visualization to convey the probabilities would be seat letters on the x-axis and probabilities on the y-axis. Panda's plot function makes that easy.


```python
# Create a list of strings to use as the x-axis labels
seats = ['Seat A', 'Seat B', 'Seat C', 'Seat D', 
         'Seat E', 'Seat F', 'Seat G', 'Seat H', 'Seat I']
```


```python
# Plot the probabilities, using 'seats' as the index as a bar chart
pd.Series(aisle_probability, index=seats).plot(kind='bar', # set y to range between 0 and 1
                                                    ylim=[0,1],
                                                    # set the figure size
                                                    figsize=[10,6],
                                                    # set the figure title
                                                    title='Probabilty of being an Aisle Seat in Economy Class')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10f1231d0>




![png](aisle_seat_probabilities_files/aisle_seat_probabilities_20_1.png)


So there we have it! If given a boarding pass with seat C you have a 86% probability of being in an aisle seat!

I hope this was helpful!
