Title: k-Fold Cross-Validating Neural Networks    
Slug: k-fold_cross-validating_neural_networks    
Summary: How to k-fold cross-validate neural networks for deep learning in Python.    
Date: 2017-09-25 12:00  
Category: Deep Learning - Keras  
Tags: Basics   
Authors: Chris Albon

If we have smaller data it can be useful to benefit from k-fold cross-validation to maximize our ability to evaluate the neural network's performance. This is possible in Keras because we can "wrap" any neural network such that it can use the evaluation features available in scikit-learn, including k-fold cross-validation. To accomplish this, we first have to create a function that returns a compiled neural network. Next we use `KerasClassifier` (if we have a classifier, if we have a regressor we can use `KerasRegressor`) to wrap the model so it can be used by scikit-learn. After this, we can use our neural network like any other scikit-learn learning algorithm (e.g. random forests, logistic regression). In our solution, we used `cross_val_score` to run a 3-fold cross-validation on our neural network.

## Preliminaries


```python
# Load libraries
import numpy as np
from keras import models
from keras import layers
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_classification

# Set random seed
np.random.seed(0)
```

    Using TensorFlow backend.


## Create Feature And Target Data


```python
# Number of features
number_of_features = 100

# Generate features matrix and target vector
features, target = make_classification(n_samples = 10000,
                                       n_features = number_of_features,
                                       n_informative = 3,
                                       n_redundant = 0,
                                       n_classes = 2,
                                       weights = [.5, .5],
                                       random_state = 0)
```

## Create Function That Constructs Neural Network


```python
# Create function returning a compiled network
def create_network():
    
    # Start neural network
    network = models.Sequential()

    # Add fully connected layer with a ReLU activation function
    network.add(layers.Dense(units=16, activation='relu', input_shape=(number_of_features,)))

    # Add fully connected layer with a ReLU activation function
    network.add(layers.Dense(units=16, activation='relu'))

    # Add fully connected layer with a sigmoid activation function
    network.add(layers.Dense(units=1, activation='sigmoid'))

    # Compile neural network
    network.compile(loss='binary_crossentropy', # Cross-entropy
                    optimizer='rmsprop', # Root Mean Square Propagation
                    metrics=['accuracy']) # Accuracy performance metric
    
    # Return compiled network
    return network
```

## Wrap Function In KerasClassifier


```python
# Wrap Keras model so it can be used by scikit-learn
neural_network = KerasClassifier(build_fn=create_network, 
                                 epochs=10, 
                                 batch_size=100, 
                                 verbose=0)
```

## Conduct k-Fold Cross-Validation Using scikit-learn


```python
# Evaluate neural network using three-fold cross-validation
cross_val_score(neural_network, features, target, cv=3)
```




    array([ 0.90491901,  0.7770777 ,  0.87068707])


