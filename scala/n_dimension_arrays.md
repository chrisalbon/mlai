Title: N Dimension Arrays   
Slug: n_dimension_arrays       
Summary: N Dimension Arrays Using Scala.  
Date: 2017-04-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create 2 x 2 Array


```scala
// Set the number of rows and columns
val rows = 2
val columns = 2

// Create an array of integers that is 2x2
val matrix = Array.ofDim[Int](rows, columns)
```


```scala
// View array
matrix
```




    Array(Array(0, 0), Array(0, 0))



## Add Values To Array


```scala
// First row, first column
matrix(0)(0) = 1

// First row, second column
matrix(0)(1) = 0

// Second row, first column
matrix(1)(0) = 0

// Second row, second column
matrix(1)(1) = 1
```


```scala
// View array
matrix
```




    Array(Array(1, 0), Array(0, 1))


