Title: Partial Functions   
Slug: partial_functions       
Summary: Partial Functions Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

`isDefinedAt` determines which inputs are accepted. `apply` is the actual operation.

## Create A Partial Function


```scala
// Create a new partial function that inputs a integer and outputs a string
val dayOfTheWeek = new PartialFunction[Int, String] {
    // Create an array with the days of the week
    val days = Array("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    
    // Only accept input integers that are between 0 and 6
    def isDefinedAt(i: Int) = i > 0 && i < 6
    
    // If accepted, return the correct day of the week string
    def apply(i: Int) = days(i-1)
}
```

## Run The Partial Function


```scala
dayOfTheWeek(2)
```




    Tuesday


