Title: Zip Together Two Lists   
Slug: zip_together_two_lists       
Summary: Zip Together Two Lists Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create Two Vectors


```scala
// Create two vectors
val firstName = Vector("Steve", "Bob", "Jack", "Jill")
val lastName = Vector("Jackson", "Dillan", "Bower", "Stein")
```

## Zip Together Vectors


```scala
// Create a new variable that zips the sequences
val fullNames = firstName zip lastName
```


```scala
// View the zipped sequences and convert to a map
fullNames
```




    Vector((Steve,Jackson), (Bob,Dillan), (Jack,Bower), (Jill,Stein))


