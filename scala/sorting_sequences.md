Title: Sorting Sequences   
Slug: sorting_sequences       
Summary: Sorting Sequences Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create Two Vectors


```scala
// Create two vectors
val ages = Vector(23,42,12,34)
val lastName = Vector("Jackson", "Dillan", "Bower", "Stein")
```

## Sort Alphabetically


```scala
// View the sequence alphabetically
lastName.sorted
```




    Vector(Bower, Dillan, Jackson, Stein)



## Sort Ascending


```scala
// View the sequence in ascending order
ages.sorted
```




    Vector(12, 23, 34, 42)



## Sort Descending


```scala
// View the sequence sorted using i > j
ages.sortWith(_ > _)
```




    Vector(42, 34, 23, 12)



## Sort By Length 


```scala
// Voew the sequence sorted by descending length
lastName.sortWith(_.length > _.length)
```




    Vector(Jackson, Dillan, Bower, Stein)


