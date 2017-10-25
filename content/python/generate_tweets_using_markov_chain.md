Title: Generate Tweets Using Markov Chains  
Slug: generate_tweets_using_markov_chain  
Summary: Generate Tweets Using Markov Chains 
Date: 2016-11-01 12:00  
Category: Python  
Tags: Other  
Authors: Chris Albon  

## Preliminaries


```python
import markovify
```

## Load Corpus

The corpus I am using is just one I found online. The corpus you choose is central to generating realistic text.


```python
# Get raw text as string
with open("brown.txt") as f:
    text = f.read()
```

## Build Markov Chain


```python
# Build the model.
text_model = markovify.Text(text)
```

# Generate One Tweet


```python
# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))
```

    Within a month, calls were still productive and most devotees of baseball attended the dozens of them.
    Even death, therefore, has a leather bolo drawn through a local rajah in 1949.
    He had a rather sharp and confident.

