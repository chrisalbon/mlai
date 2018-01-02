Title: Dimensionality Reduction With Kernel PCA  
Slug: dimensionality_reduction_with_kernel_pca  
Summary: How to reduce the dimensions of the feature matrix using kernels for machine learning in Python. 
Date: 2017-09-09 12:00  
Category: Machine Learning  
Tags: Feature Engineering
Authors: Chris Albon

<a alt="Dimensionality Reduction With Kernel PCA" href="https://machinelearningflashcards.com">
    <img src="dimensionality_reduction_with_kernel_pca/Kernel_PCA_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles
```

## Create Linearly Inseparable Data


```python
# Create linearly inseparable data
X, _ = make_circles(n_samples=1000, random_state=1, noise=0.1, factor=0.1)
```

## Conduct Kernel PCA


```python
# Apply kernal PCA with radius basis function (RBF) kernel
kpca = KernelPCA(kernel="rbf", gamma=15, n_components=1)
X_kpca = kpca.fit_transform(X)
```

## View Results


```python
print('Original number of features:', X.shape[1])
print('Reduced number of features:', X_kpca.shape[1])
```

    Original number of features: 2
    Reduced number of features: 1

