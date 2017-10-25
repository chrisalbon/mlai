Title: Save Model Training Progress    
Slug: save_model_training_progress    
Summary: How to save neural networking model training progress for deep learning in Python.    
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
from keras.callbacks import ModelCheckpoint

# Set random seed
np.random.seed(0)
```

## Load IMDB Movie Review Data


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

## Create Neural Network Architecture


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

## Compile Neural Network


```python
# Compile neural network
network.compile(loss='binary_crossentropy', # Cross-entropy
                optimizer='rmsprop', # Root Mean Square Propagation
                metrics=['accuracy']) # Accuracy performance metric
```

## Save Training Progress After Each Epoch

After every epoch `ModelCheckpoint` saves a model to the location specified by the `filepath` parameter. If we include only a filename (e.g. `models.hdf5`) that file will be overridden with the latest model every epoch. If we only wanted to save the best model according to the performance of some loss function, we can set `save_best_only=True` and `monitor='val_loss'` to not override a file if the model has a worse test loss than the previous model. Alternatively, we can save every epoch's model as its own file by including the epoch number and test loss score into the filename itself. For example if we set `filepath` to `model_{epoch:02d}_{val_loss:.2f}.hdf5`, the name of the file containing the model saved after the 11th epoch with a test loss value of 0.33 would be `model_10_0.35.hdf5` (notice that the epoch number if 0-indexed).


```python
# Set callback functions to early stop training and save the best model so far
checkpoint = [ModelCheckpoint(filepath='models.hdf5')]
```

## Train Neural Network


```python
# Train neural network
history = network.fit(train_features, # Features
                      train_target, # Target vector
                      epochs=3, # Number of epochs
                      callbacks=checkpoint, # Checkpoint
                      verbose=0, # No output
                      batch_size=100, # Number of observations per batch
                      validation_data=(test_features, test_target)) # Data for evaluation
```
