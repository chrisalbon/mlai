Title: Feedforward Neural Network For Multiclass Classification    
Slug: feedforward_neural_network_for_multiclass_classification    
Summary: How to use Keras to train a feedforward neural network for multiclass classification in Python.    
Date: 2017-09-25 12:00  
Category: Deep Learning - Keras  
Tags: Basics   
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
import numpy as np
from keras.datasets import reuters
from keras.utils.np_utils import to_categorical
from keras.preprocessing.text import Tokenizer
from keras import models
from keras import layers

# Set random seed
np.random.seed(0)
```

    Using TensorFlow backend.


## Load Movie Review Data


```python
# Set the number of features we want
number_of_features = 5000

# Load feature and target data
(train_data, train_target_vector), (test_data, test_target_vector) = reuters.load_data(num_words=number_of_features)

# Convert feature data to a one-hot encoded feature matrix
tokenizer = Tokenizer(num_words=number_of_features)
train_features = tokenizer.sequences_to_matrix(train_data, mode='binary')
test_features = tokenizer.sequences_to_matrix(test_data, mode='binary')

# One-hot encode target vector to create a target matrix
train_target = to_categorical(train_target_vector)
test_target = to_categorical(test_target_vector)
```

## Construct Neural Network Architecture

In this example we use a loss function suited to multi-class classification, the categorical cross-entropy loss function, `categorical_crossentropy`.


```python
# Start neural network
network = models.Sequential()

# Add fully connected layer with a ReLU activation function
network.add(layers.Dense(units=100, activation='relu', input_shape=(number_of_features,)))

# Add fully connected layer with a ReLU activation function
network.add(layers.Dense(units=100, activation='relu'))

# Add fully connected layer with a softmax activation function
network.add(layers.Dense(units=46, activation='softmax'))
```

## Compile Feedforward Neural Network


```python
# Compile neural network
network.compile(loss='categorical_crossentropy', # Cross-entropy
                optimizer='rmsprop', # Root Mean Square Propagation
                metrics=['accuracy']) # Accuracy performance metric
```

## Train Feedforward Neural Network


```python
# Train neural network
history = network.fit(train_features, # Features
                      train_target, # Target vector
                      epochs=3, # Three epochs
                      verbose=0, # No output
                      batch_size=100, # Number of observations per batch
                      validation_data=(test_features, test_target)) # Data to use for evaluation
```
