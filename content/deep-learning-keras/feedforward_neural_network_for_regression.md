Title: Feedforward Neural Networks For Regression    
Slug: feedforward_neural_network_for_regression    
Summary: How to train a feed-forward neural network for regression in Python.    
Date: 2017-09-25 12:00  
Category: Deep Learning - Keras  
Tags: Basics   
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras import models
from keras import layers
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# Set random seed
np.random.seed(0)
```

    Using TensorFlow backend.


## Generate Training Data


```python
# Generate features matrix and target vector
features, target = make_regression(n_samples = 10000,
                                   n_features = 3,
                                   n_informative = 3,
                                   n_targets = 1,
                                   noise = 0.0,
                                   random_state = 0)

# Divide our data into training and test sets
train_features, test_features, train_target, test_target = train_test_split(features, 
                                                                            target, 
                                                                            test_size=0.33, 
                                                                            random_state=0)
```

## Create Neural Network Architecture


```python
# Start neural network
network = models.Sequential()

# Add fully connected layer with a ReLU activation function
network.add(layers.Dense(units=32, activation='relu', input_shape=(train_features.shape[1],)))

# Add fully connected layer with a ReLU activation function
network.add(layers.Dense(units=32, activation='relu'))

# Add fully connected layer with no activation function
network.add(layers.Dense(units=1))
```

## Compile Neural Network

Because we are training a regression, we should use an appropriate loss function and evaluation metric, in our case the mean square error:

$$\operatorname {MSE}={\frac  {1}{n}}\sum _{{i=1}}^{n}({\hat  {y_{i}}}-y_{i})^{2}$$

where $n$ is the number of observations, $y_{i}$ is the true value of the target we are trying to predict, $y$, for observation $i$, and ${\hat  {y_{i}}}$ is the model's predicted value for $y_{i}$.


```python
# Compile neural network
network.compile(loss='mse', # Mean squared error
                optimizer='RMSprop', # Optimization algorithm
                metrics=['mse']) # Mean squared error
```

## Train Neural Network


```python
# Train neural network
history = network.fit(train_features, # Features
                      train_target, # Target vector
                      epochs=10, # Number of epochs
                      verbose=0, # No output
                      batch_size=100, # Number of observations per batch
                      validation_data=(test_features, test_target)) # Data for evaluation
```
