Title: Random Integer Between Two Values   
Slug: random_integer_between_two_values  
Summary: Create Integer Number Between Two Values Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

This tutorial was inspired by the awesome [Scala Cookbook](http://amzn.to/2lxbrxN) and [this](http://stackoverflow.com/posts/39402721/revisions) great StackOverflow answer.

## Load Random


```scala
// Create a value that is the random package
val random = new scala.util.Random
```

## Create A Start And End


```scala
// Create a start and end value pair
val start = -10
val end = 10
```

## Generate Random Integer Between The Start And End Values


```scala
// Then generate a random integer between 0 and the different between end and start + 1
//(to make it inclusive), then shift the value into the desired range by added the start value
start + random.nextInt( (end - start) + 1 )  
```




    1


