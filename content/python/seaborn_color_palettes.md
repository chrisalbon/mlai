Title: Color Palettes in Seaborn  
Slug: seaborn_color_palettes  
Summary: Color Palettes in Seaborn  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Visualization  
Authors: Chris Albon  

## Preliminaries


```python
import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
data = {'date': ['2014-05-01 18:47:05.069722', '2014-05-01 18:47:05.119994', '2014-05-02 18:47:05.178768', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.280592', '2014-05-03 18:47:05.332662', '2014-05-03 18:47:05.385109', '2014-05-04 18:47:05.436523', '2014-05-04 18:47:05.486877'], 
        'deaths_regiment_1': [34, 43, 14, 15, 15, 14, 31, 25, 62, 41],
        'deaths_regiment_2': [52, 66, 78, 15, 15, 5, 25, 25, 86, 1],
        'deaths_regiment_3': [13, 73, 82, 58, 52, 87, 26, 5, 56, 75],
        'deaths_regiment_4': [44, 75, 26, 15, 15, 14, 54, 25, 24, 72],
        'deaths_regiment_5': [25, 24, 25, 15, 57, 68, 21, 27, 62, 5],
        'deaths_regiment_6': [84, 84, 26, 15, 15, 14, 26, 25, 62, 24],
        'deaths_regiment_7': [46, 57, 26, 15, 15, 14, 26, 25, 62, 41]}
df = pd.DataFrame(data, columns = ['date', 'battle_deaths', 'deaths_regiment_1', 'deaths_regiment_2',
                                   'deaths_regiment_3', 'deaths_regiment_4', 'deaths_regiment_5',
                                   'deaths_regiment_6', 'deaths_regiment_7'])
df = df.set_index(df.date)
```

## View some color palettes


```python
sns.palplot(sns.color_palette("deep", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_5_0.png)



```python
sns.palplot(sns.color_palette("muted", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_6_0.png)



```python
sns.palplot(sns.color_palette("bright", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_7_0.png)



```python
sns.palplot(sns.color_palette("dark", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_8_0.png)



```python
sns.palplot(sns.color_palette("colorblind", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_9_0.png)



```python
sns.palplot(sns.color_palette("Paired", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_10_0.png)



```python
sns.palplot(sns.color_palette("BuGn", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_11_0.png)



```python
sns.palplot(sns.color_palette("GnBu", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_12_0.png)



```python
sns.palplot(sns.color_palette("OrRd", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_13_0.png)



```python
sns.palplot(sns.color_palette("PuBu", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_14_0.png)



```python
sns.palplot(sns.color_palette("YlGn", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_15_0.png)



```python
sns.palplot(sns.color_palette("YlGnBu", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_16_0.png)



```python
sns.palplot(sns.color_palette("YlOrBr", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_17_0.png)



```python
sns.palplot(sns.color_palette("YlOrRd", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_18_0.png)



```python
sns.palplot(sns.color_palette("BrBG", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_19_0.png)



```python
sns.palplot(sns.color_palette("PiYG", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_20_0.png)



```python
sns.palplot(sns.color_palette("PRGn", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_21_0.png)



```python
sns.palplot(sns.color_palette("PuOr", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_22_0.png)



```python
sns.palplot(sns.color_palette("RdBu", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_23_0.png)



```python
sns.palplot(sns.color_palette("RdGy", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_24_0.png)



```python
sns.palplot(sns.color_palette("RdYlBu", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_25_0.png)



```python
sns.palplot(sns.color_palette("RdYlGn", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_26_0.png)



```python
sns.palplot(sns.color_palette("Spectral", 10))
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_27_0.png)


## Create a color palette and set it as the current color palette


```python
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.set_palette(flatui)
sns.palplot(sns.color_palette())
```


![png](seaborn_color_palettes_files/seaborn_color_palettes_29_0.png)


## Set the color of a plot


```python
sns.tsplot([df.deaths_regiment_1, df.deaths_regiment_2, df.deaths_regiment_3, df.deaths_regiment_4,
            df.deaths_regiment_5, df.deaths_regiment_6, df.deaths_regiment_7], color="#34495e")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x116f5db70>




![png](seaborn_color_palettes_files/seaborn_color_palettes_31_1.png)

