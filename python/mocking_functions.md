Title: Mocking Functions  
Slug: mocking_functions  
Summary: Mocking Functions in Python. 
Date: 2016-01-23 12:00  
Category: Python  
Tags: Testing  
Authors: Chris Albon  

Interesting in learning more? Here are some good books on unit testing in Python: [Python Testing: Beginner's Guide](http://amzn.to/2j6dHLc) and [Python Testing Cookbook](http://amzn.to/2j6hubL).

## Preliminaries


```python
import unittest
import mock
from math import exp
```

## The Scenario

Imagine we have a function that takes in some external API or database and we want to test that function, but with fake (or mocked) inputs. The Python `mock` library lets us do that.

For this tutorial pretend that `math.exp` is some expensive operation (e.g. database query, API call, etc) that costs \$10,000 every time we use it. To test it without paying \$10,000, we can create `mock_function` which imitates the behavior of `math.exp` and allows us to test it.

## Create The Mock Function


```python
# Create a function,
def mock_function(x):
    # That returns a string.
    return 'This is not exp, but rather mock_function.'
```

## Create A Unit Test


```python
# Create a test case,
class TestRandom(unittest.TestCase):
    # where math.exp (__main__.exp is because we imported the exp module from math)
    # math.exp is mocked (replaced) by mock_function,
    @mock.patch('__main__.exp', side_effect=mock_function)
    # now create a unit test that would only be true IF the exp(4) was being mocked
    # (so we can prove that math.exp is actually being mocked)
    def test_math_exp(self, mock_function):
        # assert that math.exp(4) is actually a string, which would only be the case
        # if math.exp was being mocked by mock_function
        assert exp(4) == 'This is not exp, but rather mock_function.'
```

## Run Unit Test


```python
unittest.main(argv=['ignored', '-v'], exit=False)
```

    test_math_exp (__main__.TestRandom) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.002s
    
    OK





    <unittest.main.TestProgram at 0x104945358>


