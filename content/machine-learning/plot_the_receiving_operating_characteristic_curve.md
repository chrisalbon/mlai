Title: Plot The Receiving Operating Characteristic Curve  
Slug: plot_the_receiving_operating_characteristic_curve  
Summary: How to plot the receiving operating characteristic curve in scikit-learn for machine learning in Python.    
Date: 2017-09-15 12:00  
Category: Machine Learning  
Tags: Model Evaluation   
Authors: Chris Albon

<a alt="ROC Curve" href="https://machinelearningflashcards.com">
    <img src="plot_the_receiving_operating_characteristic_curve/Receiver_Operating_Characteristic_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
```

## Generate Features And Target


```python
# Create feature matrix and target vector
X, y = make_classification(n_samples=10000, 
                           n_features=10, 
                           n_classes=2, 
                           n_informative=3,
                           random_state=3)
```

## Split Data Intro Training And Test Sets


```python
# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)
```

## Training Binary Classifier


```python
# Create classifier
clf = LogisticRegression()

# Train model
clf.fit(X_train, y_train)
```




    LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
              intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
              penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
              verbose=0, warm_start=False)



## Create Predicted Probabilities


```python
# Get predicted probabilities
y_score = clf.predict_proba(X_test)[:,1]
```

## Plot Receiving Operating Characteristic Curve


```python
# Create true and false positive rates
false_positive_rate, true_positive_rate, threshold = roc_curve(y_test, y_score)

# Plot ROC curve
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate)
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
```


![png](plot_the_receiving_operating_characteristic_curve_files/plot_the_receiving_operating_characteristic_curve_13_0.png)

