Title: Chunk Sequence In Equal Sized Groups   
Slug: chuck_sequence_into_equal_sized_groups       
Summary: Chunk Sequence In Equal Sized Groups Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create An Array Sequence


```scala
// Create an array that contains arrays with first and last names
val ages = List(42,25,28,38,58,63,23,458,2569,584,25,25,878)
```

## Chunk Array Into Groups Of Two Elements


```scala
// Slide over sequence, create a list of two elements, then take two steps
ages.sliding(2,2).toArray
```




    Array(List(42, 25), List(28, 38), List(58, 63), List(23, 458), List(2569, 584), List(25, 25), List(878))



## Chunk Array Into Groups Of Two Elements, With Overlap


```scala
// Slide over sequence, create a list of two elements, then take one step
ages.sliding(2,1).toArray
```




    Array(List(42, 25), List(25, 28), List(28, 38), List(38, 58), List(58, 63), List(63, 23), List(23, 458), List(458, 2569), List(2569, 584), List(584, 25), List(25, 25), List(25, 878))


