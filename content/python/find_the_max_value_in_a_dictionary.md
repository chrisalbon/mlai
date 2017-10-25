Title: Find The Max Value In A Dictionary  
Slug: find_the_max_value_in_a_dictionary  
Summary: Find The Max Value In A Dictionary Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Create A Dictionary


```python
ages = {'John': 21,
        'Mike': 52,
        'Sarah': 12,
        'Bob': 43
       }
```

## Find The Maximum Value Of The Values


```python
max(zip(ages.values(), ages.keys()))
```




    (52, 'Mike')


