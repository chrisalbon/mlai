Title: Geolocate A City Or Country   
Slug: geolocate_a_city_or_country  
Summary: Geolocate a city or country.    
Date: 2016-09-21 12:00  
Category: Python  
Tags: Other  
Authors: Chris Albon  

This tutorial creates a function that attempts to take a city and country and return its latitude and longitude. But when the city is unavailable (which is often be the case), the returns the latitude and longitude of the center of the country.

## Preliminaries


```python
from geopy.geocoders import Nominatim
geolocator = Nominatim()
import numpy as np
```

## Create Geolocation Function


```python
def geolocate(city=None, country=None):
    '''
    Inputs city and country, or just country. Returns the lat/long coordinates of 
    either the city if possible, if not, then returns lat/long of the center of the country.
    '''
    
    # If the city exists,
    if city != None:
        # Try
        try:
            # To geolocate the city and country
            loc = geolocator.geocode(str(city + ',' + country))
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan
    # If the city doesn't exist
    else:
        # Try
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(country)
            # And return latitude and longitude 
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan
```

## Geolocate A City And Country


```python
# Geolocate a city and country
geolocate(city='Austin', country='USA')
```




    (30.2711286, -97.7436994)



## Geolocate Just A Country


```python
# Geolocate just a country
geolocate(country='USA')
```




    (39.7837304, -100.4458824)


