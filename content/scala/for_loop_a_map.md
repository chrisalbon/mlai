Title: For Loop A Map   
Slug: for_loop_a_map       
Summary: For Loop A Map Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create A Map


```scala
val vehicles = Map("vehicle_type" -> "Tank", 
                   "number" -> 21)
```

## Loop With Value And Index


```scala
// Create a value for the returned values, for each key and value in the map,
val numberOfVehicles = for ((key, value) <- vehicles) yield {
                         // Return the values
                         value
                       }
```


```scala
// View the returned values
numberOfVehicles
```




    List(Tank, 21)


