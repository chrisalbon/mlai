Title: Plot The Learning Curve  
Slug: plot_the_learning_curve  
Summary: How to plot the learning curve in scikit-learn for machine learning in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Model Evaluation
Authors: Chris Albon

<a alt="Plot The Learning Curve" href="https://machinelearningflashcards.com">
    <img src="plot_the_learning_curve/Learning_Curve_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
```

## Load Digits Dataset


```python
# Load data
digits = load_digits()

# Create feature matrix and target vector
X, y = digits.data, digits.target
```

## Plot Learning Curve


```python
# Create CV training and test scores for various training set sizes
train_sizes, train_scores, test_scores = learning_curve(RandomForestClassifier(), 
                                                        X, 
                                                        y,
                                                        # Number of folds in cross-validation
                                                        cv=10,
                                                        # Evaluation metric
                                                        scoring='accuracy',
                                                        # Use all computer cores
                                                        n_jobs=-1, 
                                                        # 50 different sizes of the training set
                                                        train_sizes=np.linspace(0.01, 1.0, 50))

# Create means and standard deviations of training set scores
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

# Create means and standard deviations of test set scores
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# Draw lines
plt.plot(train_sizes, train_mean, '--', color="#111111",  label="Training score")
plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

# Draw bands
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="#DDDDDD")

# Create plot
plt.title("Learning Curve")
plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), plt.legend(loc="best")
plt.tight_layout()
plt.show()
```


![png](plot_the_learning_curve_files/plot_the_learning_curve_7_0.png)

