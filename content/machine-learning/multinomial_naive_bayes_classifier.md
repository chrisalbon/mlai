Title: Multinomial Naive Bayes Classifier    
Slug: multinomial_naive_bayes_classifier   
Summary: How to train a Multinomial naive bayes classifer in Scikit-Learn   
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Naive Bayes     
Authors: Chris Albon  

Multinomial naive Bayes works similar to Gaussian naive Bayes, however the features are assumed to be multinomially distributed. In practice, this means that this classifier is commonly used when we have discrete data (e.g. movie ratings ranging 1 and 5).

## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
```

## Create Text Data


```python
# Create text
text_data = np.array(['I love Brazil. Brazil!',
                      'Brazil is best',
                      'Germany beats both'])
```

## Create Bag Of Words


```python
# Create bag of words
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

# Create feature matrix
X = bag_of_words.toarray()
```

## Create Target Vector


```python
# Create target vector
y = np.array([0,0,1])
```

## Train Multinomial Naive Bayes Classifier


```python
# Create multinomial naive Bayes object with prior probabilities of each class
clf = MultinomialNB(class_prior=[0.25, 0.5])

# Train model
model = clf.fit(X, y)
```

## Create Previously Unseen Observation


```python
# Create new observation
new_observation = [[0, 0, 0, 1, 0, 1, 0]]
```

## Predict Observation's Class


```python
# Predict new observation's class
model.predict(new_observation)
```




    array([0])


