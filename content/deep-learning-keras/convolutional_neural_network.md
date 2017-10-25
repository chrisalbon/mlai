Title: Convolutional Neural Network    
Slug: convolutional_neural_network    
Summary: How to train a deep convolutional neural network with Keras in Python.    
Date: 2017-09-25 12:00  
Category: Deep Learning - Keras  
Tags: Basics   
Authors: Chris Albon

## Preliminaries


```python
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K 

# Set that the color channel value will be first
K.set_image_data_format('channels_first')

# Set seed
np.random.seed(0)
```

## Load MNIST Image Data


```python
# Set image information
channels = 1
height = 28
width = 28

# Load data and target from MNIST data
(train_data, train_target), (test_data, test_target) = mnist.load_data()

# Reshape training image data into features
train_data = train_data.reshape(train_data.shape[0], channels, height, width)

# Reshape test image data into features
test_data = test_data.reshape(test_data.shape[0], channels, height, width)

# Rescale pixel intensity to between 0 and 1
train_features = train_data / 255
test_features = test_data / 255

# One-hot encode target
train_target = np_utils.to_categorical(train_target)
test_target = np_utils.to_categorical(test_target)
number_of_classes = test_target.shape[1]
```

## Create Convolutional Neural Network Architecture

Convolutional neural networks (also called ConvNets) are a popular type of network that has proven very effective at computer vision (e.g. recognizing cats, dogs, planes, and even hot dogs). It is completely possible to use feedforward neural networks on images, where each pixel is a feature. However, when doing so we run into two major problems. 

First, a feedforward neural networks do not take into account the spatial structure of the pixels. For example, in a 10x10 pixel image we might convert it into a vector of 100 pixel features, and in this case feedforward would consider the first feature (e.g. pixel value) to have the same relationship with the 10th feature as the 11th feature. However, in reality the 10th feature represents a pixel on the far side of the image as the first feature, while the 11th feature represents the pixel immediately below the first pixel. 

Second, and relatedly, feedforward neural networks learn global relationships in the features instead of local patterns. In more practical terms, this means that feedforward neural networks are not able to detect an object regardless of where it appears in an image. For example, imagine we are training a neural network to recognize faces, these faces might appear anywhere in the image from the upper right to the middle to the lower left. The power of convolutional neural networks is their ability handle both of these issues (and others).


```python
# Start neural network
network = Sequential()

# Add convolutional layer with 64 filters, a 5x5 window, and ReLU activation function
network.add(Conv2D(filters=64, kernel_size=(5, 5), input_shape=(channels, width, height), activation='relu'))

# Add max pooling layer with a 2x2 window
network.add(MaxPooling2D(pool_size=(2, 2)))

# Add dropout layer
network.add(Dropout(0.5))

# Add layer to flatten input
network.add(Flatten())

# # Add fully connected layer of 128 units with a ReLU activation function
network.add(Dense(128, activation='relu'))

# Add dropout layer
network.add(Dropout(0.5))

# Add fully connected layer with a softmax activation function
network.add(Dense(number_of_classes, activation='softmax'))
```

## Compile Convolutional Neural Network


```python
# Compile neural network
network.compile(loss='categorical_crossentropy', # Cross-entropy
                optimizer='rmsprop', # Root Mean Square Propagation
                metrics=['accuracy']) # Accuracy performance metric
```

## Train Convolutional Neural Network


```python
# Train neural network
network.fit(train_features, # Features
            train_target, # Target
            epochs=2, # Number of epochs
            verbose=0, # Don't print description after each epoch
            batch_size=1000, # Number of observations per batch
            validation_data=(test_features, test_target)) # Data for evaluation
```




    <keras.callbacks.History at 0x129039748>


