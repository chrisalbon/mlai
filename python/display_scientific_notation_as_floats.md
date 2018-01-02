Title: Display Scientific Notation As Floats    
Slug: display_scientific_notation_as_floats     
Summary: How to display a number in scientific notation as a float.     
Date: 2017-09-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon 

## Create Values


```python
# Create a numbers in scientific notation
value_scientific_notation = 6.32000000e-03

# Create a vector of numbers in scientific notation
vector_scientific_notation = [6.32000000e-03,
                              1.80000000e+01,
                              2.31000000e+00,
                              0.00000000e+00,
                              5.38000000e-01,
                              6.57500000e+00,
                              6.52000000e+01,
                              4.09000000e+00,
                              1.00000000e+00,
                              2.96000000e+02,
                              1.53000000e+01,
                              3.96900000e+02,
                              4.98000000e+00]
```

## Display Values As Floats


```python
# Display value as a float
'{:f}'.format(value_scientific_notation)
```




    '0.006320'




```python
# Display vector values as floats
['{:f}'.format(x) for x in vector_scientific_notation]
```




    ['0.006320',
     '18.000000',
     '2.310000',
     '0.000000',
     '0.538000',
     '6.575000',
     '65.200000',
     '4.090000',
     '1.000000',
     '296.000000',
     '15.300000',
     '396.900000',
     '4.980000']


