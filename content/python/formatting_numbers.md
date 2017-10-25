Title: Formatting Numbers  
Slug: formatting_numbers  
Summary: Formatting Numbers Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Create A Long Number


```python
annual_revenue = 9282904.9282872782
```

## Format Number


```python
# Format rounded to two decimal places
format(annual_revenue, '0.2f')
```




    '9282904.93'




```python
# Format with commas and  rounded to one decimal place
format(annual_revenue, '0,.1f')
```




    '9,282,904.9'




```python
# Format as scientific notation
format(annual_revenue, 'e')
```




    '9.282905e+06'




```python
# Format as scientific notation rounded to two deciminals
format(annual_revenue, '0.2E')
```




    '9.28E+06'


