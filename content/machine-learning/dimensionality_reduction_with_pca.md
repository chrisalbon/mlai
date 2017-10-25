Title: Dimensionality Reduction With PCA  
Slug: dimensionality_reduction_with_pca  
Summary: How to reduce the dimensions of the feature matrix for machine learning in Python. 
Date: 2017-09-13 12:00  
Category: Machine Learning  
Tags: Feature Engineering
Authors: Chris Albon

<a alt="Dimensionality Reduction With PCA" href="https://machinelearningflashcards.com">
    <img src="dimensionality_reduction_with_pca/Principal_Component_Analysis_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets
```

## Load Data


```python
# Load the data
digits = datasets.load_digits()
```

## Standardize Feature Values


```python
# Standardize the feature matrix
X = StandardScaler().fit_transform(digits.data)
```

## Conduct Principal Component Analysis


```python
# Create a PCA that will retain 99% of the variance
pca = PCA(n_components=0.99, whiten=True)

# Conduct PCA
X_pca = pca.fit_transform(X)
```

## View Results


```python
# Show results
print('Original number of features:', X.shape[1])
print('Reduced number of features:', X_pca.shape[1])
```

    Original number of features: 64
    Reduced number of features: 54

