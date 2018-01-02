Title: Data Structure Basics  
Slug: data_structure_basics  
Summary: Data Structure Basics  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Lists

"A list is a data structure that holds an ordered collection of items i.e. you can store a sequence of items in a list." - A Byte Of Python

Lists are mutable.


```python
# Create a list of countries, then print the results
allies = ['USA','UK','France','New Zealand',
          'Australia','Canada','Poland']; allies
```




    ['USA', 'UK', 'France', 'New Zealand', 'Australia', 'Canada', 'Poland']




```python
# Print the length of the list
len(allies)
```




    7




```python
# Add an item to the list, then print the results
allies.append('China'); allies
```




    ['USA',
     'UK',
     'France',
     'New Zealand',
     'Australia',
     'Canada',
     'Poland',
     'China']




```python
# Sort list, then print the results
allies.sort(); allies
```




    ['Australia',
     'Canada',
     'China',
     'France',
     'New Zealand',
     'Poland',
     'UK',
     'USA']




```python
# Reverse sort list, then print the results
allies.reverse(); allies
```




    ['USA',
     'UK',
     'Poland',
     'New Zealand',
     'France',
     'China',
     'Canada',
     'Australia']




```python
# View the first item of the list
allies[0]
```




    'USA'




```python
# View the last item of the list
allies[-1]
```




    'Australia'




```python
# Delete the item in the list
del allies[0]; allies
```




    ['UK', 'Poland', 'New Zealand', 'France', 'China', 'Canada', 'Australia']




```python
# Add a numeric value to a list of strings
allies.append(3442); allies
```




    ['UK', 'Poland', 'New Zealand', 'France', 'China', 'Canada', 'Australia', 3442]



## Tuples

"Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain an heterogeneous sequence of elements that are accessed via unpacking (or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list." - Python Documentation

"Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences." - StackOverflow

Parentheses are optional, but useful.


```python
# Create a tuple of state names
usa = ('Texas', 'California', 'Maryland'); usa
```




    ('Texas', 'California', 'Maryland')




```python
# Create a tuple of countries
# (notice the USA has a state names in the nested tuple)
countries = ('canada', 'mexico', usa); countries
```




    ('canada', 'mexico', ('Texas', 'California', 'Maryland'))




```python
# View the third item of the top tuple
countries[2]
```




    ('Texas', 'California', 'Maryland')




```python
# View the third item of the third tuple
countries[2][2]
```




    'Maryland'



## Dictionaries

"A dictionary is like an address-book where you can find the address or contact details of a person by knowing only his/her name i.e. we associate keys (name) with values (details). Note that the key must be unique just like you cannot find out the correct information if you have two persons with the exact same name." - A Byte Of Python


```python
# Create a dictionary with key:value combos
staff = {'Chris' : 'chris@stater.org',
         'Jake' : 'jake@stater.org',
         'Ashley' : 'ashley@stater.org',
         'Shelly' : 'shelly@stater.org'
        }
```


```python
# Print the value using the key
staff['Chris']
```




    'chris@stater.org'




```python
# Delete a dictionary entry based on the key
del staff['Chris']; staff
```




    {'Ashley': 'ashley@stater.org',
     'Jake': 'jake@stater.org',
     'Shelly': 'shelly@stater.org'}




```python
# Add an item to the dictionary
staff['Guido'] = 'guido@python.org'; staff
```




    {'Ashley': 'ashley@stater.org',
     'Guido': 'guido@python.org',
     'Jake': 'jake@stater.org',
     'Shelly': 'shelly@stater.org'}



## Sets

Sets are unordered collections of simple objects.


```python
# Create a set of BRI countries
BRI = set(['brazil', 'russia', 'india'])
```


```python
# Is India in the set BRI?
'india' in BRI
```




    True




```python
# Is the US in the set BRI?
'usa' in BRI
```




    False




```python
# Create a copy of BRI called BRIC
BRIC = BRI.copy()
```


```python
# Add China to BRIC
BRIC.add('china')
```


```python
# Is BRIC a super-set of BRI?
BRIC.issuperset(BRI)
```




    True




```python
# Remove Russia from BRI
BRI.remove('russia')
```


```python
# What items are the union of BRI and BRIC?
BRI & BRIC
```




    {'brazil', 'india'}


