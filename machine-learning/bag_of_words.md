Title: Bag Of Words  
Slug: bag_of_words  
Summary: How to encode unstructured text data as bags of words for machine learning in Python. 
Date: 2017-09-09 12:00  
Category: Machine Learning  
Tags: Preprocessing Text
Authors: Chris Albon

<a alt="Bag Of Words" href="https://machinelearningflashcards.com">
    <img src="bag_of_words/Bag_Of_Words_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load library
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
```

## Create Text Data


```python
# Create text
text_data = np.array(['I love Brazil. Brazil!',
                      'Sweden is best',
                      'Germany beats both'])
```

## Create Bag Of Words


```python
# Create the bag of words feature matrix
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

# Show feature matrix
bag_of_words.toarray()
```




    array([[0, 0, 0, 2, 0, 0, 1, 0],
           [0, 1, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 0, 0]], dtype=int64)



## View Bag Of Words Matrix Column Headers


```python
# Get feature names
feature_names = count.get_feature_names()

# View feature names
feature_names
```




    ['beats', 'best', 'both', 'brazil', 'germany', 'is', 'love', 'sweden']



## View As A Data Frame


```python
# Create data frame
pd.DataFrame(bag_of_words.toarray(), columns=feature_names)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>beats</th>
      <th>best</th>
      <th>both</th>
      <th>brazil</th>
      <th>germany</th>
      <th>is</th>
      <th>love</th>
      <th>sweden</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


