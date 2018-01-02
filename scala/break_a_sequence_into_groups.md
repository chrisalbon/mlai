Title: Break A Sequence Into Groups   
Slug: break_a_sequence_into_groups       
Summary: Break A Sequence Into Groups Using Scala.  
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

## Group Array By Anonymous Function


```scala
// If an element is even, return True, if not, return False
val isEven = ages.groupBy(_ % 2 == 0)
```

## View Groups


```scala
// View group that is evens
evensOdds(true)
```




    List(42, 28, 38, 58, 458, 584, 878)




```scala
// View group that is odds
evensOdds(false)
```




    List(25, 63, 23, 2569, 25, 25)


