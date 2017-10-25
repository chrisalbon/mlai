Title: Detecting Outliers  
Slug: detecting_outliers     
Summary: How to detect outliers for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs
```

## Create Data


```python
# Create simulated data
X, _ = make_blobs(n_samples = 10,
                  n_features = 2,
                  centers = 1,
                  random_state = 1)

# Replace the first observation's values with extreme values
X[0,0] = 10000
X[0,1] = 10000
```

## Detect Outliers

`EllipticEnvelope` assumes the data is normally distributed and based on that assumption "draws" an ellipse around the data, classifying any observation inside the ellipse as an inlier (labeled as  `1`) and any observation outside the ellipse as an outlier (labeled as `-1`). A major limitation of this approach is the need to specify a `contamination` parameter which is the proportion of observations that are outliers, a value that we don't know.


```python
# Create detector
outlier_detector = EllipticEnvelope(contamination=.1)

# Fit detector
outlier_detector.fit(X)

# Predict outliers
outlier_detector.predict(X)
```




    array([-1,  1,  1,  1,  1,  1,  1,  1,  1,  1])


