Title: Test For A Specific Exception  
Slug: test_for_a_specific_exception  
Summary: Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Testing  
Authors: Chris Albon  

## Preliminaries


```python
import unittest
```

## Create A Function To Test


```python
def add(x, y):
    return x + y
```

## Create Test Case


```python
# Create a test case
class TestAdd(unittest.TestCase):
    # Create the unit test
    def test_input_string(self):
        # Test To make sure a TypeError exception is raised
        self.assertRaises(TypeError, add('Banana', 'Boat'))
```

## Run Test


```python
# Run the unit test (and don't shut down the Jupyter Notebook)
unittest.main(argv=['ignored', '-v'], exit=False)
```

    test_input_string (__main__.TestAdd) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.002s
    
    OK





    <unittest.main.TestProgram at 0x104855320>


