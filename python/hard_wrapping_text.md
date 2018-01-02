Title: Hard Wrapping Text  
Slug: hard_wrapping_text  
Summary: Hard Wrapping Text Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Preliminaries


```python
import textwrap
```

## Create Text


```python
# Create some text
excerpt = 'Then there was the bad weather. It would come in one day when the fall was over. We would have to shut the windows in the night against the rain and the cold wind would strip the leaves from the trees in the Place Contrescarpe. The leaves lay sodden in the rain and the wind drove the rain against the big green autobus at the terminal and the Café des Amateurs was crowded and the windows misted over from the heat and the smoke inside.'
```

## Hard Wrap Text


```python
# Hard wrap the excerpt at 50 characters
print(textwrap.fill(excerpt, 50))
```

    Then there was the bad weather. It would come in
    one day when the fall was over. We would have to
    shut the windows in the night against the rain and
    the cold wind would strip the leaves from the
    trees in the Place Contrescarpe. The leaves lay
    sodden in the rain and the wind drove the rain
    against the big green autobus at the terminal and
    the Café des Amateurs was crowded and the windows
    misted over from the heat and the smoke inside.

