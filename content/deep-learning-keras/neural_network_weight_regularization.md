Title: Neural Network Weight Regularization    
Slug: neural_network_weight_regularization    
Summary: How reduce overfitting with weight regularization of a neural network in Python.    
Date: 2017-09-25 12:00  
Category: Deep Learning - Keras  
Tags: Basics   
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
import numpy as np
from keras.datasets import imdb
from keras.preprocessing.text import Tokenizer
from keras import models
from keras import layers
from keras import regularizers

# Set random seed
np.random.seed(0)
```

    Using TensorFlow backend.


## Load Movie Review Text Data


```python
# Set the number of features we want
number_of_features = 1000

# Load data and target vector from movie review data
(train_data, train_target), (test_data, test_target) = imdb.load_data(num_words=number_of_features)

# Convert movie review data to a one-hot encoded feature matrix
tokenizer = Tokenizer(num_words=number_of_features)
train_features = tokenizer.sequences_to_matrix(train_data, mode='binary')
test_features = tokenizer.sequences_to_matrix(test_data, mode='binary')
```

## Create Neural Network Architecture With Weight Regularization

In Keras, we can add a weight regularization by including using including `kernel_regularizer=regularizers.l2(0.01)` a later. In this example, `0.01` determines how much we penalize higher parameter values.


```python
# Start neural network
network = models.Sequential()

# Add fully connected layer with a ReLU activation function and L2 regularization
network.add(layers.Dense(units=16, 
                         activation='relu', 
                         kernel_regularizer=regularizers.l2(0.01),
                         input_shape=(number_of_features,)))

# Add fully connected layer with a ReLU activation function and L2 regularization
network.add(layers.Dense(units=16, 
                         kernel_regularizer=regularizers.l2(0.01),
                         activation='relu'))


```

## Compile Neural Network


```python
# Add fully connected layer with a sigmoid activation function
network.add(layers.Dense(units=1, activation='sigmoid'))# Compile neural network
network.compile(loss='binary_crossentropy', # Cross-entropy
                optimizer='rmsprop', # Root Mean Square Propagation
                metrics=['accuracy']) # Accuracy performance metric
```

## Train Neural Network


```python
# Train neural network
history = network.fit(train_features, # Features
                      train_target, # Target vector
                      epochs=3, # Number of epochs
                      verbose=0, # No output
                      batch_size=100, # Number of observations per batch
                      validation_data=(test_features, test_target)) # Data for evaluation
```
