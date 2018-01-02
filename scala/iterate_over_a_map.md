Title: Iterate Over A Map   
Slug: iterate_over_a_map       
Summary: Iterate Over A Map Using Scala.  
Date: 2017-04-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create A Map


```scala
// Create a map with three key value pairs
val prices = Map("Video Card" -> 200.00,
                 "Motherboard" -> 400.00,
                 "CPU" -> 100.00)
```

## Loop Over A Map


```scala
// for each key and value in prices
for ((k,v) <- prices) yield {
    // Return the value plus 100
    v+100
}
```




    List(300.0, 500.0, 200.0)



## Apply Function To Each Map Value


```scala
// Increase each value in the map by 1000
prices.mapValues(_+1000)
```




    Map(Video Card -> 1200.0, Motherboard -> 1400.0, CPU -> 1100.0)


