Title: Lambda Functions  
Slug: lambda_functions  
Summary: Lambda Functions  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

In Python it is possible to string lambda functions together.

### Create a series, called pipeline, that contains three mini functions


```python
pipeline = [lambda x: x **2 - 1 + 5,
            lambda x: x **20 - 2 + 3,
            lambda x: x **200 - 1 + 4]
```

### For each item in pipeline, run the lambda function with x = 3


```python
for f in pipeline:
    print(f(3))
```

    13
    3486784402
    265613988875874769338781322035779626829233452653394495974574961739092490901302182994384699044004

