Title: Bessel's Correction 
Slug: bessels_correction  
Summary: A short explanation of Bessel's Correction. 
Date: 2016-08-19 12:00  
Category: Statistics  
Tags: Basics  
Authors: Chris Albon  

Bessel's correction is the reason we use $n-1$ instead of $n$ in the calculations of sample variance and sample standard deviation.

Sample variance:

$$ s^2 = \frac {1}{n-1} \sum_{i=1}^n  \left(x_i - \overline{x} \right)^ 2 $$

When we calculate sample variance, we are attempting to estimate the population variance, an unknown value. To make this estimate, we estimate this unknown population variance from the mean of the squared deviations of samples from the overall sample mean. A negative sideffect of this estimation technique is that, because we are taking a sample, we are a more likely to observe observations with a smaller deviation because they are more common (e.g. they are the center of the distribution). The means that by definiton we will underestimate the population variance.

Friedrich Bessel figured out that by multiplying a biased (uncorrected) sample variance $s_n^2 = \frac {1}{n} \sum_{i=1}^n  \left(x_i - \overline{x} \right)^ 2$ by $\frac{n}{n-1}$ we will be able to reduce that bias and thus be able to make an accurate estimate of the population variance and standard deviation. The end result of that multiplication is the unbiased sample variance.
