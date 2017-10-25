Title: Mathematical Operations  
Slug: math_operations  
Summary: Mathematical Operations  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

### Import the math module


```python
import math
```

### Display the value of pi.


```python
math.pi
```




    3.141592653589793



### Display the value of e.


```python
math.e
```




    2.718281828459045



### Sine, cosine, and tangent


```python
math.sin(2 * math.pi / 180)
```




    0.03489949670250097



### Exponent


```python
2 ** 4, pow(2, 4)
```




    (16, 16)



### Absolute value


```python
abs(-20)
```




    20



### Summation


```python
sum((1, 2, 3, 4))
```




    10



### Minimum


```python
min(3, 9, 10, 12)
```




    3



### Maximum


```python
max(3, 5, 10, 15)
```




    15



### Floor


```python
math.floor(2.949)
```




    2



### Truncate (drop decimal digits)


```python
math.trunc(32.09292)
```




    32



### Truncate (integer conversion)


```python
int(3.292838)
```




    3



### Round to an integrer


```python
round(2.943), round(2.499)
```




    (3, 2)



### Round by 2 digits


```python
round(2.569, 2)
```




    2.57


