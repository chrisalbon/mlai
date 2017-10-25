Title: LSTM Recurrent Neural Network    
Slug: lstm_recurrent_neural_network    
Summary: How to add dropout to a neural networking for deep learning in Python.    
Date: 2017-09-25 12:00  
Category: Deep Learning - Keras  
Tags: Basics   
Authors: Chris Albon

Oftentimes we have text data that we want to classify. While it is possible to use a type of convolutional network, we are going to focus on a more popular option: the recurrent neural network. The key feature of recurrent neural networks is that information loops back in the network. This gives recurrent neural networks a type of memory it can use to better understand sequential data. A popular choice type of recurrent neural network is the long short-term memory (LSTM) network which allows for information to loop backwards in the network.

## Preliminaries


```python
# Load libraries
import numpy as np
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras import models
from keras import layers

# Set random seed
np.random.seed(0)
```

    Using TensorFlow backend.


## Load Dataset On Movie Review Text


```python
# Set the number of features we want
number_of_features = 1000

# Load data and target vector from movie review data
(train_data, train_target), (test_data, test_target) = imdb.load_data(num_words=number_of_features)

# Use padding or truncation to make each observation have 400 features
train_features = sequence.pad_sequences(train_data, maxlen=400)
test_features = sequence.pad_sequences(test_data, maxlen=400)
```

## View First Observation's Raw Data


```python
# View first observation
print(train_data[0])
```

    [1, 14, 22, 16, 43, 530, 973, 2, 2, 65, 458, 2, 66, 2, 4, 173, 36, 256, 5, 25, 100, 43, 838, 112, 50, 670, 2, 9, 35, 480, 284, 5, 150, 4, 172, 112, 167, 2, 336, 385, 39, 4, 172, 2, 2, 17, 546, 38, 13, 447, 4, 192, 50, 16, 6, 147, 2, 19, 14, 22, 4, 2, 2, 469, 4, 22, 71, 87, 12, 16, 43, 530, 38, 76, 15, 13, 2, 4, 22, 17, 515, 17, 12, 16, 626, 18, 2, 5, 62, 386, 12, 8, 316, 8, 106, 5, 4, 2, 2, 16, 480, 66, 2, 33, 4, 130, 12, 16, 38, 619, 5, 25, 124, 51, 36, 135, 48, 25, 2, 33, 6, 22, 12, 215, 28, 77, 52, 5, 14, 407, 16, 82, 2, 8, 4, 107, 117, 2, 15, 256, 4, 2, 7, 2, 5, 723, 36, 71, 43, 530, 476, 26, 400, 317, 46, 7, 4, 2, 2, 13, 104, 88, 4, 381, 15, 297, 98, 32, 2, 56, 26, 141, 6, 194, 2, 18, 4, 226, 22, 21, 134, 476, 26, 480, 5, 144, 30, 2, 18, 51, 36, 28, 224, 92, 25, 104, 4, 226, 65, 16, 38, 2, 88, 12, 16, 283, 5, 16, 2, 113, 103, 32, 15, 16, 2, 19, 178, 32]


## View First Observation's Feature Data


```python
# View first observation
test_features[0]
```




    array([  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   1,  89,  27,   2,   2,  17, 199, 132,   5,   2,
            16,   2,  24,   8, 760,   4,   2,   7,   4,  22,   2,   2,  16,
             2,  17,   2,   7,   2,   2,   9,   4,   2,   8,  14, 991,  13,
           877,  38,  19,  27, 239,  13, 100, 235,  61, 483,   2,   4,   7,
             4,  20, 131,   2,  72,   8,  14, 251,  27,   2,   7, 308,  16,
           735,   2,  17,  29, 144,  28,  77,   2,  18,  12], dtype=int32)



## Create LSTM Neural Network Architecture


```python
# Start neural network
network = models.Sequential()

# Add an embedding layer
network.add(layers.Embedding(input_dim=number_of_features, output_dim=128))

# Add a long short-term memory layer with 128 units
network.add(layers.LSTM(units=128))

# Add fully connected layer with a sigmoid activation function
network.add(layers.Dense(units=1, activation='sigmoid'))
```

## Compule LSTM Neural Network Architecture


```python
# Compile neural network
network.compile(loss='binary_crossentropy', # Cross-entropy
                optimizer='Adam', # Adam optimization
                metrics=['accuracy']) # Accuracy performance metric
```

## Train LSTM Neural Network Architecture


```python
# Train neural network
history = network.fit(train_features, # Features
                      train_target, # Target
                      epochs=3, # Number of epochs
                      verbose=0, # Do not print description after each epoch
                      batch_size=1000, # Number of observations per batch
                      validation_data=(test_features, test_target)) # Data for evaluation
```
