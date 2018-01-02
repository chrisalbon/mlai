Title: Chi-Squared For Feature Selection  
Slug: chi-squared_for_feature_selection  
Summary: How to remove irrelevant features using chi-squared for machine learning in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Feature Selection
Authors: Chris Albon

<a alt="chi-squared_for_feature_selection" href="https://machinelearningflashcards.com">
    <img src="chi-squared_for_feature_selection/Chi-Squared_For_Feature_Selection_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
```

## Load Data


```python
# Load iris data
iris = load_iris()

# Create features and target
X = iris.data
y = iris.target

# Convert to categorical data by converting data to integers
X = X.astype(int)
```

## Compare Chi-Squared Statistics


```python
# Select two features with highest chi-squared statistics
chi2_selector = SelectKBest(chi2, k=2)
X_kbest = chi2_selector.fit_transform(X, y)
```

## View Results


```python
# Show results
print('Original number of features:', X.shape[1])
print('Reduced number of features:', X_kbest.shape[1])
```

    Original number of features: 4
    Reduced number of features: 2

