Title: Set The Color Of A Matplotlib Plot  
Slug: set_the_color_of_a_matplotlib  
Summary: Set The Color Of A Matplotlib Plot  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Visualization  
Authors: Chris Albon  

### Import numpy and matplotlib.pyplot


```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
```

### Create some simulated data.


```python
n = 100
r = 2 * np.random.rand(n)
theta = 2 * np.pi * np.random.rand(n)
area = 200 * r**2 * np.random.rand(n)
colors = theta
```

### Create a scatterplot using the a colormap.
Full list of colormaps: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps


```python
c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.RdYlGn)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_6_0.png)



```python
c1 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.Blues)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_7_0.png)



```python
c2 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.BrBG)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_8_0.png)



```python
c3 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.Greens)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_9_0.png)



```python
c4 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.RdGy)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_10_0.png)



```python
c5 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.YlOrRd)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_11_0.png)



```python
c6 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.autumn)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_12_0.png)



```python
c7 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.binary)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_13_0.png)



```python
c8 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.gist_earth)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_14_0.png)



```python
c9 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.gist_heat)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_15_0.png)



```python
c10 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.hot)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_16_0.png)



```python
c11 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.spring)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_17_0.png)



```python
c12 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.summer)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_18_0.png)



```python
c12 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.winter)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_19_0.png)



```python
c13 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.bone)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_20_0.png)



```python
c14 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.cool)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_21_0.png)



```python
c15 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.YlGn)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_22_0.png)



```python
c16 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.RdBu)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_23_0.png)



```python
c17 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.PuOr)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_24_0.png)



```python
c18 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.Oranges)
```


![png](set_the_color_of_a_matplotlib_files/set_the_color_of_a_matplotlib_25_0.png)

