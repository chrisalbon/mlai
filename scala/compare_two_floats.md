Title: Compare Two Floats  
Slug: compare_two_floats  
Summary: Compare Two Floats Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

This tutorial was inspired by the awesome [Scala Cookbook](http://amzn.to/2lxbrxN).

## Create Two Float Values


```scala
// Create a value
val price_old = 2.343232

// Create a value that is very slight different
val price_new = 2.343231
```

## Create A Function That Compares Two Floats


```scala
// Define a function called ~= that contains three arguments: two numbers and a precision level,
def ~=(x: Double, y: Double, precision: Double) = {
    // If the absolute difference is less than the precision level, return true, otherwise return false
    if ((x - y).abs < precision) true else false
}
```

## Apply Function With High Precision


```scala
// Compare price_old and price_new with 0.000001 precision
~=(price_old, price_new, 0.000001)
```




    false



## Apply Function With Low Precision


```scala
// Compare price_old and price_new with 0.1 precision
~=(price_old, price_new, 0.1)
```




    true


