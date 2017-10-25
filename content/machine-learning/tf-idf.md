Title: Term Frequency Inverse Document Frequency  
Slug: tf-idf  
Summary: How to weight word importance in unstructured text data as bags of words for machine learning in Python. 
Date: 2017-09-09 12:00  
Category: Machine Learning  
Tags: Preprocessing Text
Authors: Chris Albon

<a alt="tf-idf" href="https://machinelearningflashcards.com">
    <img src="tf-idf/TF-IDF_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
```

## Create Text Data


```python
# Create text
text_data = np.array(['I love Brazil. Brazil!',
                      'Sweden is best',
                      'Germany beats both'])
```

## Create Feature Matrix


```python
# Create the tf-idf feature matrix
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)

# Show tf-idf feature matrix
feature_matrix.toarray()
```




    array([[ 0.        ,  0.        ,  0.        ,  0.89442719,  0.        ,
             0.        ,  0.4472136 ,  0.        ],
           [ 0.        ,  0.57735027,  0.        ,  0.        ,  0.        ,
             0.57735027,  0.        ,  0.57735027],
           [ 0.57735027,  0.        ,  0.57735027,  0.        ,  0.57735027,
             0.        ,  0.        ,  0.        ]])




```python
# Show tf-idf feature matrix
tfidf.get_feature_names()
```




    ['beats', 'best', 'both', 'brazil', 'germany', 'is', 'love', 'sweden']



## View Feature Matrix As Data Frame


```python
# Create data frame
pd.DataFrame(feature_matrix.toarray(), columns=tfidf.get_feature_names())
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
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.894427</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.447214</td>
      <td>0.00000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.00000</td>
      <td>0.57735</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.57735</td>
      <td>0.000000</td>
      <td>0.57735</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.57735</td>
      <td>0.00000</td>
      <td>0.57735</td>
      <td>0.000000</td>
      <td>0.57735</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>0.00000</td>
    </tr>
  </tbody>
</table>
</div>


