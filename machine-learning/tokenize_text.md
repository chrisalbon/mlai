Title: Tokenize Text  
Slug: tokenize_text  
Summary: How to tokenize text from unstructured text data for machine learning in Python.   
Date: 2016-09-08 12:00  
Category: Machine Learning  
Tags: Preprocessing Text
Authors: Chris Albon

## Preliminaries


```python
# Load library
from nltk.tokenize import word_tokenize, sent_tokenize
```

## Create Text Data


```python
# Create text
string = "The science of today is the technology of tomorrow. Tomorrow is today."
```

## Tokenize Words


```python
# Tokenize words
word_tokenize(string)
```




    ['The',
     'science',
     'of',
     'today',
     'is',
     'the',
     'technology',
     'of',
     'tomorrow',
     '.',
     'Tomorrow',
     'is',
     'today',
     '.']



## Tokenize Sentences


```python
# Tokenize sentences
sent_tokenize(string)
```




    ['The science of today is the technology of tomorrow.', 'Tomorrow is today.']


