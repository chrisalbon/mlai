Title: Search A Map   
Slug: search_a_map       
Summary: Search A Map Using Scala.  
Date: 2017-04-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create A Map


```scala
// Create an immutable map with three key value pairs
val staff = Map("CEO" -> "Judith Jackson", 
                "CFO" -> "Sally Shields",
                "CTO" -> "Steven Miller")
```

## Test If Key Exists


```scala
// Test if key exists
staff.contains("CTO")
```




    true



## Test If Value Exists


```scala
// Test is any value exists which contains part of a string
staff.valuesIterator.exists(_.contains("Miller"))
```




    true


