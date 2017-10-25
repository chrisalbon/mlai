Title: Find Largest Key Or Value In A Map   
Slug: find_largest_key_or_value_in_a_map       
Summary: Find Largest Key Or Value In A Map Using Scala.  
Date: 2017-04-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create A Map


```scala
// Create an immutable map with three key value pairs
val numbers = Map(1 -> 100, 
                  2 -> 200,
                  3 -> 300)
```

## Find Largest Key


```scala
// Find largest key
numbers.max
```




    (3,300)



## Find Largest Value


```scala
// Find the largest value
numbers.valuesIterator.max
```




    300


