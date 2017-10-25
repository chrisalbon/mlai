Title: Naive Bayes Classifier From Scratch   
Slug: naive_bayes_classifier_from_scratch   
Summary: How to build a naive bayes classifier from scratch in Python.   
Date: 2016-12-12 12:00    
Category: Machine Learning   
Tags: Naive Bayes   
Authors: Chris Albon    

Naive bayes is simple classifier known for doing well when only a small number of observations is available. In this tutorial we will create a gaussian naive bayes classifier from scratch and use it to predict the class of a previously unseen data point. This tutorial is based on an example on Wikipedia's [naive bayes classifier page](https://en.wikipedia.org/wiki/Naive_Bayes_classifier), I have implemented it in Python and tweaked some notation to improve explanation. 

## Preliminaries


```python
import pandas as pd
import numpy as np
```

## Create Data

Our dataset is contains data on eight individuals. We will use the dataset to construct a classifier that takes in the height, weight, and foot size of an individual and outputs a prediction for their gender.


```python
# Create an empty dataframe
data = pd.DataFrame()

# Create our target variable
data['Gender'] = ['male','male','male','male','female','female','female','female']

# Create our feature variables
data['Height'] = [6,5.92,5.58,5.92,5,5.5,5.42,5.75]
data['Weight'] = [180,190,170,165,100,150,130,150]
data['Foot_Size'] = [12,11,12,10,6,8,7,9]

# View the data
data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Height</th>
      <th>Weight</th>
      <th>Foot_Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>male</td>
      <td>6.00</td>
      <td>180</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>male</td>
      <td>5.92</td>
      <td>190</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>male</td>
      <td>5.58</td>
      <td>170</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>male</td>
      <td>5.92</td>
      <td>165</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>female</td>
      <td>5.00</td>
      <td>100</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>female</td>
      <td>5.50</td>
      <td>150</td>
      <td>8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>female</td>
      <td>5.42</td>
      <td>130</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>female</td>
      <td>5.75</td>
      <td>150</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



The dataset above is used to construct our classifier. Below we will create a new person for whom we know their feature values but not their gender. Our goal is to predict their gender.


```python
# Create an empty dataframe
person = pd.DataFrame()

# Create some feature values for this single row
person['Height'] = [6]
person['Weight'] = [130]
person['Foot_Size'] = [8]

# View the data 
person
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Height</th>
      <th>Weight</th>
      <th>Foot_Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6</td>
      <td>130</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



## Bayes Theorem

Bayes theorem is a famous equation that allows us to make predictions based on data. Here is the classic version of the Bayes theorem:

$$\displaystyle P(A\mid B)={\frac {P(B\mid A)\,P(A)}{P(B)}}$$

This might be too abstract, so let us replace some of the variables to make it more concrete. In a bayes classifier, we are interested in finding out the class (e.g. male or female, spam or ham) of an observation _given_ the data:

$$p(\text{class} \mid \mathbf {\text{data}} )={\frac {p(\mathbf {\text{data}} \mid \text{class}) * p(\text{class})}{p(\mathbf {\text{data}} )}}$$

where: 

- $\text{class}$ is a particular class (e.g. male)
- $\mathbf {\text{data}}$ is an observation's data
- $p(\text{class} \mid \mathbf {\text{data}} )$ is called the posterior
- $p(\text{data|class})$ is called the likelihood
- $p(\text{class})$ is called the prior
- $p(\mathbf {\text{data}} )$ is called the marginal probability

In a bayes classifier, we calculate the posterior (technically we only calculate the numerator of the posterior, but ignore that for now) for every class for each observation. Then, classify the observation based on the class with the largest posterior value. In our example, we have one observation to predict and two possible classes (e.g. male and female), therefore we will calculate two posteriors: one for male and one for female.

$$p(\text{person is male} \mid \mathbf {\text{person's data}} )={\frac {p(\mathbf {\text{person's data}} \mid \text{person is male}) * p(\text{person is male})}{p(\mathbf {\text{person's data}} )}}$$

$$p(\text{person is female} \mid \mathbf {\text{person's data}} )={\frac {p(\mathbf {\text{person's data}} \mid \text{person is female}) * p(\text{person is female})}{p(\mathbf {\text{person's data}} )}}$$

## Gaussian Naive Bayes Classifier

A gaussian naive bayes is probably the most popular type of bayes classifier. To explain what the name means, let us look at what the bayes equations looks like when we apply our two classes (male and female) and three feature variables (height, weight, and footsize):

$${\displaystyle {\text{posterior (male)}}={\frac {P({\text{male}})\,p({\text{height}}\mid{\text{male}})\,p({\text{weight}}\mid{\text{male}})\,p({\text{foot size}}\mid{\text{male}})}{\text{marginal probability}}}}$$

$${\displaystyle {\text{posterior (female)}}={\frac {P({\text{female}})\,p({\text{height}}\mid{\text{female}})\,p({\text{weight}}\mid{\text{female}})\,p({\text{foot size}}\mid{\text{female}})}{\text{marginal probability}}}}$$

Now let us unpack the top equation a bit:

- $P({\text{male}})$ is the prior probabilities. It is, as you can see, simply the probability an observation is male. This is just the number of males in the dataset divided by the total number of people in the dataset.
- $p({\text{height}}\mid{\text{female}})\,p({\text{weight}}\mid{\text{female}})\,p({\text{foot size}}\mid{\text{female}})$ is the likelihood. Notice that we have unpacked $\mathbf {\text{person's data}}$ so it is now every feature in the dataset. The "gaussian" and "naive" come from two assumptions present in this likelihood:
    1. If you look each term in the likelihood you will notice that we assume each feature is uncorrelated from each other. That is, foot size is independent of weight or height etc.. This is obviously not true, and is a "naive" assumption - hence the name "naive bayes."
    2. Second, we assume have that the value of the features (e.g. the height of women, the weight of women) are normally (gaussian) distributed. This means that $p(\text{height}\mid\text{female})$ is calculated by inputing the required parameters into the probability density function of the normal distribution: 

$$ 
p(\text{height}\mid\text{female})=\frac{1}{\sqrt{2\pi\text{variance of female height in the data}}}\,e^{ -\frac{(\text{observation's height}-\text{average height of females in the data})^2}{2\text{variance of female height in the data}} }
$$

- $\text{marginal probability}$ is probably one of the most confusing parts of bayesian approaches. In toy examples (including ours) it is completely possible to calculate the marginal probability. However, in many real-world cases, it is either extremely difficult or impossible to find the value of the marginal probability (explaining why is beyond the scope of this tutorial). This is not as much of a problem for our classifier as you might think. Why? Because we don't care what the true posterior value is, we only care which class has a the highest posterior value. And because the marginal probability is the same for all classes 1) we can ignore the denominator, 2) calculate only the posterior's numerator for each class, and 3) pick the largest numerator. That is, we can ignore the posterior's denominator and make a prediction solely on the relative values of the posterior's numerator.

Okay! Theory over. Now let us start calculating all the different parts of the bayes equations.

## Calculate Priors

Priors can be either constants or probability distributions. In our example is the simply the probability of being a gender. Calculating this is simple:


```python
# Number of males
n_male = data['Gender'][data['Gender'] == 'male'].count()

# Number of males
n_female = data['Gender'][data['Gender'] == 'female'].count()

# Total rows
total_ppl = data['Gender'].count()
```


```python
# Number of males divided by the total rows
P_male = n_male/total_ppl

# Number of females divided by the total rows
P_female = n_female/total_ppl
```

## Calculate Likelihood

Remember that each term (e.g. $p(\text{height}\mid\text{female})$) in our likelihood is assumed to be a normal pdf. For example:

$$ 
p(\text{height}\mid\text{female})=\frac{1}{\sqrt{2\pi\text{variance of female height in the data}}}\,e^{ -\frac{(\text{observation's height}-\text{average height of females in the data})^2}{2\text{variance of female height in the data}} }
$$

This means that for each class (e.g. female) and feature (e.g. height) combination we need to calculate the variance and mean value from the data. Pandas makes this easy:


```python
# Group the data by gender and calculate the means of each feature
data_means = data.groupby('Gender').mean()

# View the values
data_means
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Height</th>
      <th>Weight</th>
      <th>Foot_Size</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>5.4175</td>
      <td>132.50</td>
      <td>7.50</td>
    </tr>
    <tr>
      <th>male</th>
      <td>5.8550</td>
      <td>176.25</td>
      <td>11.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Group the data by gender and calculate the variance of each feature
data_variance = data.groupby('Gender').var()

# View the values
data_variance
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Height</th>
      <th>Weight</th>
      <th>Foot_Size</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.097225</td>
      <td>558.333333</td>
      <td>1.666667</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.035033</td>
      <td>122.916667</td>
      <td>0.916667</td>
    </tr>
  </tbody>
</table>
</div>



Now we can create all the variables we need. The code below might look complex but all we are doing is creating a variable out of each cell in both of the tables above.


```python
# Means for male
male_height_mean = data_means['Height'][data_variance.index == 'male'].values[0]
male_weight_mean = data_means['Weight'][data_variance.index == 'male'].values[0]
male_footsize_mean = data_means['Foot_Size'][data_variance.index == 'male'].values[0]

# Variance for male
male_height_variance = data_variance['Height'][data_variance.index == 'male'].values[0]
male_weight_variance = data_variance['Weight'][data_variance.index == 'male'].values[0]
male_footsize_variance = data_variance['Foot_Size'][data_variance.index == 'male'].values[0]

# Means for female
female_height_mean = data_means['Height'][data_variance.index == 'female'].values[0]
female_weight_mean = data_means['Weight'][data_variance.index == 'female'].values[0]
female_footsize_mean = data_means['Foot_Size'][data_variance.index == 'female'].values[0]

# Variance for female
female_height_variance = data_variance['Height'][data_variance.index == 'female'].values[0]
female_weight_variance = data_variance['Weight'][data_variance.index == 'female'].values[0]
female_footsize_variance = data_variance['Foot_Size'][data_variance.index == 'female'].values[0]
```

Finally, we need to create a function to calculate the probability density of each of the terms of the likelihood (e.g. $p(\text{height}\mid\text{female})$).


```python
# Create a function that calculates p(x | y):
def p_x_given_y(x, mean_y, variance_y):

    # Input the arguments into a probability density function
    p = 1/(np.sqrt(2*np.pi*variance_y)) * np.exp((-(x-mean_y)**2)/(2*variance_y))
    
    # return p
    return p
```

## Apply Bayes Classifier To New Data Point

Alright! Our bayes classifier is ready. Remember that since we can ignore the marginal probability (the demoninator), what we are actually calculating is this:

$${\displaystyle {\text{numerator of the posterior}}={P({\text{female}})\,p({\text{height}}\mid{\text{female}})\,p({\text{weight}}\mid{\text{female}})\,p({\text{foot size}}\mid{\text{female}})}{}}$$

To do this, we just need to plug in the values of the unclassified person (height = 6), the variables of the dataset (e.g. mean of female height), and the function (`p_x_given_y`) we made above:


```python
# Numerator of the posterior if the unclassified observation is a male
P_male * \
p_x_given_y(person['Height'][0], male_height_mean, male_height_variance) * \
p_x_given_y(person['Weight'][0], male_weight_mean, male_weight_variance) * \
p_x_given_y(person['Foot_Size'][0], male_footsize_mean, male_footsize_variance)
```




    6.1970718438780782e-09




```python
# Numerator of the posterior if the unclassified observation is a female
P_female * \
p_x_given_y(person['Height'][0], female_height_mean, female_height_variance) * \
p_x_given_y(person['Weight'][0], female_weight_mean, female_weight_variance) * \
p_x_given_y(person['Foot_Size'][0], female_footsize_mean, female_footsize_variance)
```




    0.00053779091836300176



Because the numerator of the posterior for female is greater than male, then we predict that the person is female.
