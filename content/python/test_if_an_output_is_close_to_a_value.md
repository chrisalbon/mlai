Title: Test If Output Is Close To A Value  
Slug: test_if_an_output_is_close_to_a_value  
Summary: Test if an output is close to a value in Python. 
Date: 2016-01-23 12:00  
Category: Python  
Tags: Testing  
Authors: Chris Albon  

Interesting in learning more? Here are some good books on unit testing in Python: [Python Testing: Beginner's Guide](http://amzn.to/2j6dHLc) and [Python Testing Cookbook](http://amzn.to/2j6hubL).

## Preliminaries


```python
import unittest
import sys
```

## Create Function To Be Tested


```python
def add(x, y):
    return x + y
```

## Create Test


```python
# Create a test case
class TestAdd(unittest.TestCase):
    # Create the unit test
    def test_add_two_floats_roughly_equals_11(self):
        # Test if add(4.48293848, 6.5023845) return roughly (to 1 place) 11 (actual product: 10.98532298)
        self.assertAlmostEqual(11, add(4.48293848, 6.5023845), places=1)
```

## Run Test


```python
# Run the unit test (and don't shut down the Jupyter Notebook)
unittest.main(argv=['ignored', '-v'], exit=False)
```

    test_add_two_floats_roughly_equals_11 (__main__.TestAdd) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    OK





    <unittest.main.TestProgram at 0x1049191d0>


