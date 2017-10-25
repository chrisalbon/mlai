Title: Feedforward Neural Network For Binary Classification    
Slug: feedforward_neural_network_for_binary_classification    
Summary: How to use Keras to train a feedforward neural network for binary classification in Python.    
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

# Set random seed
np.random.seed(0)
```

    Using TensorFlow backend.


## Load Movie Review Data


```python
# Set the number of features we want
number_of_features = 1000

# Load data and target vector from movie review data
(train_data, train_target), (test_data, test_target) = imdb.load_data(num_words=number_of_features)

# Convert movie review data to one-hot encoded feature matrix
tokenizer = Tokenizer(num_words=number_of_features)
train_features = tokenizer.sequences_to_matrix(train_data, mode='binary')
test_features = tokenizer.sequences_to_matrix(test_data, mode='binary')
```

## Construct Neural Network Architecture

Because this is a binary classification problem, one common choice is to use the sigmoid activation function in a one-unit output layer.


```python
# Start neural network
network = models.Sequential()

# Add fully connected layer with a ReLU activation function
network.add(layers.Dense(units=16, activation='relu', input_shape=(number_of_features,)))

# Add fully connected layer with a ReLU activation function
network.add(layers.Dense(units=16, activation='relu'))

# Add fully connected layer with a sigmoid activation function
network.add(layers.Dense(units=1, activation='sigmoid'))
```

## Compile Feedforward Neural Network


```python
# Compile neural network
network.compile(loss='binary_crossentropy', # Cross-entropy
                optimizer='rmsprop', # Root Mean Square Propagation
                metrics=['accuracy']) # Accuracy performance metric
```

## Train Feedforward Neural Network

In Keras, we train our neural network using the `fit` method. There are six significant parameters to define. The first two parameters are the features and target vector of the training data. 

The `epochs` parameter defines how many epochs to use when training the data. `verbose` determines how much information is outputted during the training process, with `0` being no out, `1` outputting a progress bar, and `2` one log line per epoch. `batch_size` sets the number of observations to propagate through the network before updating the parameters.

Finally, we held out a test set of data to use to evaluate the model. These test features and test target vector can be arguments of the `validation_data`, which will use them for evaluation. Alternatively, we could have used `validation_split` to define what fraction of the training data we want to hold out for evaluation.

In scikit-learn `fit` method returned a trained model, however in Keras the `fit` method returns a `History` object containing the loss values and performance metrics at each epoch.


```python
# Train neural network
history = network.fit(train_features, # Features
                      train_target, # Target vector
                      epochs=3, # Number of epochs
                      verbose=1, # Print description after each epoch
                      batch_size=100, # Number of observations per batch
                      validation_data=(test_features, test_target)) # Data for evaluation
```

    Train on 25000 samples, validate on 25000 samples
    Epoch 1/3
    25000/25000 [==============================] - 1s - loss: 0.4215 - acc: 0.8107 - val_loss: 0.3388 - val_acc: 0.8556
    Epoch 2/3
    25000/25000 [==============================] - 1s - loss: 0.3240 - acc: 0.8646 - val_loss: 0.3256 - val_acc: 0.8630
    Epoch 3/3
    25000/25000 [==============================] - 1s - loss: 0.3117 - acc: 0.8702 - val_loss: 0.3264 - val_acc: 0.8601

