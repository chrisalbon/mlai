Title: Iterate An Ifelse Over A List  
Slug: iterate_ifelse_over_list  
Summary: Iterate An Ifelse Over A List  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Create some data


```python
word_list = ['Egypt', 'Watching', 'Eleanor']

vowels = ['A', 'E', 'I', 'O', 'U']
```

## Create a for loop


```python
# for each item in the word_list,
for word in word_list:
    # if any word starts with e, where e is vowels,
    if any([word.startswith(e) for e in vowels]):
        # then print is valid,
        print('Is valid')
    # if not,    
    else:
        # print invalid
        print('Invalid')
```

    Is valid
    Invalid
    Is valid

