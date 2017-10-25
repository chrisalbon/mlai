Title: Streaming Data Pipeline  
Slug: streaming_data_pipeline  
Summary: Streaming Data Pipeline Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Create Some Raw Data


```python
raw_data = [1,2,3,4,5,6,7,8,9,10]
```

## Create Data Processing Functions


```python
# Define a generator that yields input+6
def add_6(numbers):
    for x in numbers:
        output = x+6
        yield output

# Define a generator that yields input-2
def subtract_2(numbers):
    for x in numbers:
        output = x-2
        yield output
        
# Define a generator that yields input*100        
def multiply_by_100(numbers):
    for x in numbers:
        output = x*100
        yield output
```

## Create Data Pipeline


```python
# Step 1 of the pipeline
step1 = add_6(raw_data)

# Step 2 of the pipeline
step2 = subtract_2(step1)

# Step 3 of the pipeline
pipeline = multiply_by_100(step2)
```

## Send First Two Pieces Of Raw Data Through Pipeline


```python
# First element of the raw data
next(pipeline)
```




    500




```python
# Second element of the raw data
next(pipeline)
```




    600



## Send All Raw Data Through Pipeline


```python
# Process all data
for raw_data in pipeline:
    print(raw_data)
```

    700
    800
    900
    1000
    1100
    1200
    1300
    1400

