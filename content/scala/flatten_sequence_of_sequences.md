Title: Flatten Sequence Of Sequences   
Slug: flatten_sequence_of_sequences       
Summary: Flatten Sequence Of Sequences Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create An Array Sequence


```scala
// Create an array that contains arrays with first and last names
val fullNames = Array(
    Array("Jason", "Miller"),
    Array("Jason", "Miller"), // Duplicate
    Array("Sally", "Fields"),
    Array("Betty", "Johnson")
)
```

## Flatten The Sequence 


```scala
// Flatten the sequence
fullNames.flatten
```




    Array(Jason, Miller, Jason, Miller, Sally, Fields, Betty, Johnson)



## Flatten The Sequence And Only Keep Unique Values


```scala
// Flatten the sequence and remove any duplicates
fullNames.flatten.distinct
```




    Array(Jason, Miller, Sally, Fields, Betty, Johnson)


