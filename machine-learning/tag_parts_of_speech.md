Title: Tag Parts Of Speech  
Slug: tag_parts_of_speech  
Summary: How to tag parts of speech in unstructured text data for machine learning in Python.   
Date: 2016-09-09 12:00  
Category: Machine Learning  
Tags: Preprocessing Text
  
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from nltk import pos_tag
from nltk import word_tokenize
```

## Create Text Data


```python
# Create text
text_data = "Chris loved outdoor running"
```

## Tag Parts Of Speech


```python
# Use pre-trained part of speech tagger
text_tagged = pos_tag(word_tokenize(text_data))

# Show parts of speech
text_tagged
```




    [('Chris', 'NNP'), ('loved', 'VBD'), ('outdoor', 'RP'), ('running', 'VBG')]



## Common Penn Treebank Parts Of Speech Tags

The output is a list of tuples with the word and the tag of the part of speech. NLTK uses the Penn Treebank parts for speech tags.

<table>
  <tr>
    <th>Tag</th>
    <th>Part Of Speech</th>
  </tr>
  <tr>
    <td>NNP</td>
    <td>Proper noun, singular</td>
  </tr>
    <tr>
    <td>NN</td>
    <td>Noun, singular or mass</td>
  </tr>
    <tr>
    <td>RB</td>
    <td>Adverb</td>
  </tr>
    <tr>
    <td>VBD</td>
    <td>Verb, past tense</td>
  </tr>
    <tr>
    <td>VBG</td>
    <td>Verb, gerund or present participle</td>
  </tr>
    <tr>
    <td>JJ</td>
    <td>Adjective</td>
  </tr>
      <tr>
    <td>PRP</td>
    <td>Personal pronoun</td>
  </tr>
</table>
