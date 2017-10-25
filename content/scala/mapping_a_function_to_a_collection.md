Title: Mapping A Function To A Collection   
Slug: mapping_a_function_to_a_collection       
Summary: Mapping A Function To A Collection Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Preliminaries


```scala
import scala.collection.mutable.ArrayBuffer
```

## Create Collection


```scala
// Create an array of strings
var birds = ArrayBuffer("Hawk", "Condor", "Eagle", "Pigeon")
```

## Create Function


```scala
// Create a function that returns the length of a string
val getLength = (i: String) => i.length
```

## Map The Function To The Collection


```scala
// Map the function to the array
birds.map(getLength)
```




    ArrayBuffer(4, 6, 5, 6)



## Map An Anonymous Function To The Collection


```scala
// Map the anonymous function to the collection
birds.map(_.toUpperCase)
```




    ArrayBuffer(HAWK, CONDOR, EAGLE, PIGEON)


