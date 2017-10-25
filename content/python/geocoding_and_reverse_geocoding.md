Title: Geocoding And Reverse Geocoding  
Slug: geocoding_and_reverse_geocoding  
Summary: Geocoding And Reverse Geocoding  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

Geocoding (converting a physical address or location into latitude/longitude) and reverse geocoding (converting a lat/long to a physical address or location) are common tasks when working with geo-data.

Python offers a number of packages to make the task incredibly easy. In the tutorial below, I use pygeocoder, a wrapper for Google's geo-API, to both geocode and reverse geocode.

## Preliminaries

First we want to load the packages we will want to use in the script. Specifically, I am loading pygeocoder for its geo-functionality, pandas for its dataframe structures, and numpy for its missing value (np.nan) functionality.


```python
# Load packages
from pygeocoder import Geocoder
import pandas as pd
import numpy as np
```

## Create some simulated geo data

Geo-data comes in a wide variety of forms, in this case we have a Python dictionary of five latitude and longitude strings, with each coordinate in a coordinate pair separated by a comma.


```python
# Create a dictionary of raw data
data = {'Site 1': '31.336968, -109.560959',
        'Site 2': '31.347745, -108.229963',
        'Site 3': '32.277621, -107.734724',
        'Site 4': '31.655494, -106.420484',
        'Site 5': '30.295053, -104.014528'}
```

While technically unnecessary, because I originally come from R, I am a big fan of dataframes, so let us turn the dictionary of simulated data into a dataframe.


```python
# Convert the dictionary into a pandas dataframe
df = pd.DataFrame.from_dict(data, orient='index')
```


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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Site 4</th>
      <td>31.655494, -106.420484</td>
    </tr>
    <tr>
      <th>Site 3</th>
      <td>32.277621, -107.734724</td>
    </tr>
    <tr>
      <th>Site 1</th>
      <td>31.336968, -109.560959</td>
    </tr>
    <tr>
      <th>Site 5</th>
      <td>30.295053, -104.014528</td>
    </tr>
    <tr>
      <th>Site 2</th>
      <td>31.347745, -108.229963</td>
    </tr>
  </tbody>
</table>
</div>



You can see now that we have a a dataframe with five rows, with each now containing a string of latitude and longitude. Before we can work with the data, we'll need to 1) seperate the strings into latitude and longitude and 2) convert them into floats. The function below does just that.


```python
# Create two lists for the loop results to be placed
lat = []
lon = []

# For each row in a varible,
for row in df[0]:
    # Try to,
    try:
        # Split the row by comma, convert to float, and append
        # everything before the comma to lat
        lat.append(float(row.split(',')[0]))
        # Split the row by comma, convert to float, and append
        # everything after the comma to lon
        lon.append(float(row.split(',')[1]))
    # But if you get an error
    except:
        # append a missing value to lat
        lat.append(np.NaN)
        # append a missing value to lon
        lon.append(np.NaN)

# Create two new columns from lat and lon
df['latitude'] = lat
df['longitude'] = lon
```

Let's take a took a what we have now.


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
      <th>0</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Site 4</th>
      <td>31.655494, -106.420484</td>
      <td>31.655494</td>
      <td>-106.420484</td>
    </tr>
    <tr>
      <th>Site 3</th>
      <td>32.277621, -107.734724</td>
      <td>32.277621</td>
      <td>-107.734724</td>
    </tr>
    <tr>
      <th>Site 1</th>
      <td>31.336968, -109.560959</td>
      <td>31.336968</td>
      <td>-109.560959</td>
    </tr>
    <tr>
      <th>Site 5</th>
      <td>30.295053, -104.014528</td>
      <td>30.295053</td>
      <td>-104.014528</td>
    </tr>
    <tr>
      <th>Site 2</th>
      <td>31.347745, -108.229963</td>
      <td>31.347745</td>
      <td>-108.229963</td>
    </tr>
  </tbody>
</table>
</div>



Awesome. This is exactly what we want to see, one column of floats for latitude and one column of floats for longitude.

## Reverse Geocoding

To reverse geocode, we feed a specific latitude and longitude pair, in this case the first row (indexed as '0') into pygeocoder's reverse_geocoder function. 


```python
# Convert longitude and latitude to a location
results = Geocoder.reverse_geocode(df['latitude'][0], df['longitude'][0])
```

Now we can take can start pulling out the data that we want.


```python
# Print the lat/long
results.coordinates
```




    (31.6556534, -106.4204309)




```python
# Print the city
results.city
```




    'Ciudad Juárez'




```python
# Print the country
results.country
```




    'Mexico'




```python
# Print the street address (if applicable)
results.street_address
```


```python
# Print the admin1 level
results.administrative_area_level_1
```




    'Chihuahua'



## Geocoding

For geocoding, we need to submit a string containing an address or location (such as a city) into the geocode function. However, not all strings are formatted in a way that Google's geo-API can make sense of them. We can text if an input is valid by using the .geocode().valid_address function.


```python
# Verify that an address is valid (i.e. in Google's system)
Geocoder.geocode("4207 N Washington Ave, Douglas, AZ 85607").valid_address
```




    True



Because the output was True, we now know that this is a valid address and thus can print the latitude and longitude coordinates.


```python
# Print the lat/long
results.coordinates
```




    (31.6556534, -106.4204309)



But even more interesting, once the address is processed by the Google geo API, we can parse it and easily separate street numbers, street names, etc. 


```python
# Find the lat/long of a certain address
result = Geocoder.geocode("7250 South Tucson Boulevard, Tucson, AZ 85756")
```


```python
# Print the street number
result.street_number
```




    '7250'




```python
# Print the street name
result.route
```




    'South Tucson Boulevard'



And there you have it. Python makes this entire process easy and inserting it into an analysis only takes a few minutes. Good luck!
