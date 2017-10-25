Title: ANOVA F-value For Feature Selection  
Slug: anova_f-value_for_feature_selection  
Summary: How to remove irrelevant features using ANOVA F-value for machine learning in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Feature Selection
Authors: Chris Albon

If the features are categorical, calculate a chi-square ($\chi^{2}$) statistic between each feature and the target vector. However, if the features are quantitative, compute the ANOVA F-value between each feature and the target vector. 

The F-value scores examine if, when we group the numerical feature by the target vector, the means for each group are significantly different. 

## Preliminaries


```python
# Load libraries
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
```

## Load Data


```python
# Load iris data
iris = load_iris()

# Create features and target
X = iris.data
y = iris.target
```

## Select Features With Best ANOVA F-Values


```python
# Create an SelectKBest object to select features with two best ANOVA F-Values
fvalue_selector = SelectKBest(f_classif, k=2)

# Apply the SelectKBest object to the features and target
X_kbest = fvalue_selector.fit_transform(X, y)
```

## View Results


```python
# Show results
print('Original number of features:', X.shape[1])
print('Reduced number of features:', X_kbest.shape[1])
```

    Original number of features: 4
    Reduced number of features: 2

