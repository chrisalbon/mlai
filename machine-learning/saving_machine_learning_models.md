Title: Saving Machine Learning Models  
Slug: saving_machine_learning_models  
Summary: Saving Machine Learning Models from scikit learn.   
Date: 2016-09-22 12:00  
Category: Machine Learning  
Tags: Basics  
Authors: Chris Albon

In scikit there are two main ways to save a model for future use: a pickle string and a pickled model as a file.

## Preliminaries


```python
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pickle
from sklearn.externals import joblib
```

## Load Data


```python
# Load the iris data
iris = datasets.load_iris()

# Create a matrix, X, of features and a vector, y.
X, y = iris.data, iris.target
```

## Train Model


```python
# Train a naive logistic regression model
clf = LogisticRegression(random_state=0)
clf.fit(X, y)  
```




    LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
              intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
              penalty='l2', random_state=0, solver='liblinear', tol=0.0001,
              verbose=0, warm_start=False)



## Save To String Using Pickle


```python
# Save the trained model as a pickle string.
saved_model = pickle.dumps(clf)
```


```python
# View the pickled model
saved_model
```




    b'\x80\x03csklearn.linear_model.logistic\nLogisticRegression\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00penaltyq\x03X\x02\x00\x00\x00l2q\x04X\x0b\x00\x00\x00multi_classq\x05X\x03\x00\x00\x00ovrq\x06X\x08\x00\x00\x00max_iterq\x07KdX\x08\x00\x00\x00classes_q\x08cnumpy.core.multiarray\n_reconstruct\nq\tcnumpy\nndarray\nq\nK\x00\x85q\x0bC\x01bq\x0c\x87q\rRq\x0e(K\x01K\x03\x85q\x0fcnumpy\ndtype\nq\x10X\x02\x00\x00\x00i8q\x11K\x00K\x01\x87q\x12Rq\x13(K\x03X\x01\x00\x00\x00<q\x14NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00tq\x15b\x89C\x18\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00q\x16tq\x17bX\x07\x00\x00\x00n_iter_q\x18h\th\nK\x00\x85q\x19h\x0c\x87q\x1aRq\x1b(K\x01K\x01\x85q\x1ch\x10X\x02\x00\x00\x00i4q\x1dK\x00K\x01\x87q\x1eRq\x1f(K\x03h\x14NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00tq b\x89C\x04\x07\x00\x00\x00q!tq"bX\x06\x00\x00\x00n_jobsq#K\x01X\x11\x00\x00\x00intercept_scalingq$K\x01X\x03\x00\x00\x00tolq%G?\x1a6\xe2\xeb\x1cC-X\x07\x00\x00\x00verboseq&K\x00X\x04\x00\x00\x00dualq\'\x89X\x0c\x00\x00\x00random_stateq(K\x00X\x05\x00\x00\x00coef_q)h\th\nK\x00\x85q*h\x0c\x87q+Rq,(K\x01K\x03K\x04\x86q-h\x10X\x02\x00\x00\x00f8q.K\x00K\x01\x87q/Rq0(K\x03h\x14NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00tq1b\x88C`\x9a\x1c\x904+\x8f\xda?v5\xf6\x7f9\xaa\xda?FVL\xe5\x05R\xfb\xbf\xf6\xad\xd9^ya\xf7?\x89\x86\x10B\x03\x9d\xf9\xbf\x7f\xa7x\xf5\\\x8c\xf8\xbf\x8b$8y\xdd\x18\x02\xc0\xac\x8f\xee\xd9+|\xe2?\\\x10\xf2\xcc\x8c\xc4\x03@\xda\xb0;l,w\xf0\xbf8_\xe7W*+\xf6\xbf\xefT`-lq\x04@q2tq3bX\n\x00\x00\x00intercept_q4h\th\nK\x00\x85q5h\x0c\x87q6Rq7(K\x01K\x03\x85q8h0\x89C\x18\xd4\x86D\x03\xb1\xff\xd0?\xa2\xcc=I\xe5]\xf1?\x84\'\xad\x8dxo\xf3\xbfq9tq:bX\n\x00\x00\x00warm_startq;\x89X\x01\x00\x00\x00Cq<G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00fit_interceptq=\x88X\x06\x00\x00\x00solverq>X\t\x00\x00\x00liblinearq?X\x0c\x00\x00\x00class_weightq@Nub.'




```python
# Load the pickled model
clf_from_pickle = pickle.loads(saved_model)

# Use the loaded pickled model to make predictions
clf_from_pickle.predict(X)
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1,
           1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])



## Save To Pickled File Using joblib


```python
# Save the model as a pickle in a file
joblib.dump(clf, 'filename.pkl') 
```




    ['filename.pkl',
     'filename.pkl_01.npy',
     'filename.pkl_02.npy',
     'filename.pkl_03.npy',
     'filename.pkl_04.npy']




```python
# Load the model from the file
clf_from_joblib = joblib.load('filename.pkl') 
```


```python
# Use the loaded model to make predictions
clf_from_joblib.predict(X)
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1,
           1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])


