Title: Breaking Up String Variables  
Slug: breaking_up_string_variables  
Summary: Breaking Up String Variables  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

### Basic name assignment


```python
variableName = 'This is a string.'
```

### List assignment


```python
One, Two, Three = [1, 2, 3]
```

### Break up a string into variables


```python
firstLetter, secondLetter, thirdLetter, fourthLetter = 'Bark'
```


```python
firstLetter
```




    'B'




```python
secondLetter
```




    'a'




```python
thirdLetter
```




    'r'




```python
fourthLetter
```




    'k'



### Breaking up a number into separate variables


```python
firstNumber, secondNumber, thirdNumber, fourthNumber = '9485'
```


```python
firstNumber
```




    '9'




```python
secondNumber
```




    '4'




```python
thirdNumber
```




    '8'




```python
fourthNumber
```




    '5'



### Assign the first letter of 'spam' into varible a, assign all the remaining letters to variable b


```python
a, *b = 'spam'
a
```




    's'




```python
b
```




    ['p', 'a', 'm']


