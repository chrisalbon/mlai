Title: Cleaning Text  
Slug: cleaning_text  
Summary: Cleaning Text  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Create some raw text


```python
# Create a list of three strings.
incoming_reports = ["We are attacking on their left flank but are losing many men.", 
               "We cannot see the enemy army. Nothing else to report.", 
               "We are ready to attack but are waiting for your orders."]
```

## Seperate by word


```python
# import word tokenizer
from nltk.tokenize import word_tokenize

# Apply word_tokenize to each element of the list called incoming_reports
tokenized_reports = [word_tokenize(report) for report in incoming_reports]

# View tokenized_reports
tokenized_reports
```




    [['We',
      'are',
      'attacking',
      'on',
      'their',
      'left',
      'flank',
      'but',
      'are',
      'losing',
      'many',
      'men',
      '.'],
     ['We',
      'can',
      'not',
      'see',
      'the',
      'enemy',
      'army',
      '.',
      'Nothing',
      'else',
      'to',
      'report',
      '.'],
     ['We',
      'are',
      'ready',
      'to',
      'attack',
      'but',
      'are',
      'waiting',
      'for',
      'your',
      'orders',
      '.']]




```python
# Import regex
import re

# Import string
import string


regex = re.compile('[%s]' % re.escape(string.punctuation)) #see documentation here: http://docs.python.org/2/library/string.html

tokenized_reports_no_punctuation = []

for review in tokenized_reports:
    
    new_review = []
    for token in review: 
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    
    tokenized_reports_no_punctuation.append(new_review)
    
tokenized_reports_no_punctuation
```




    [['We',
      'are',
      'attacking',
      'on',
      'their',
      'left',
      'flank',
      'but',
      'are',
      'losing',
      'many',
      'men'],
     ['We',
      'can',
      'not',
      'see',
      'the',
      'enemy',
      'army',
      'Nothing',
      'else',
      'to',
      'report'],
     ['We',
      'are',
      'ready',
      'to',
      'attack',
      'but',
      'are',
      'waiting',
      'for',
      'your',
      'orders']]



## Remove filler words


```python
from nltk.corpus import stopwords

tokenized_reports_no_stopwords = []
for report in tokenized_reports_no_punctuation:
    new_term_vector = []
    for word in report:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    tokenized_reports_no_stopwords.append(new_term_vector)
            
tokenized_reports_no_stopwords
```




    [['We', 'attacking', 'left', 'flank', 'losing', 'many', 'men'],
     ['We', 'see', 'enemy', 'army', 'Nothing', 'else', 'report'],
     ['We', 'ready', 'attack', 'waiting', 'orders']]


