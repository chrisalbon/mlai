Title: Filter A Sequence   
Slug: filter_a_sequence       
Summary: Filter A Sequence Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create An Array Sequence


```scala
// Create an array that contains arrays with first and last names
val ages = Array(42,25,28,38,58,63,23,458,2569,584,25,25,878)
```

## Elements Less Than 100


```scala
ages.filter(_ < 100)
```




    Array(42, 25, 28, 38, 58, 63, 23, 25, 25)



## Elements Greater Than 100


```scala
ages.filter(_ >= 100)
```




    Array(458, 2569, 584, 878)



## Elements That Are Even


```scala
ages.filter(_ % 2 == 0)
```




    Array(42, 28, 38, 58, 458, 584, 878)


