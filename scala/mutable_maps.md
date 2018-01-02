Title: Mutable Maps   
Slug: mutable_maps       
Summary: Mutable Maps Using Scala.  
Date: 2017-04-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create A Mutable Map


```scala
val army = collection.mutable.Map(
    "Tank" -> "A-1 Abrams",
    "Aircraft" -> "F35",
    "Ship" -> "Nimitz Class"
)
```

## Add An Element


```scala
// Add an element
army += ("APC" -> "Bradley IFC")

// Add an element (alternative)
army.put("Weapon", "M60")
```




    None



## Add Multiple Elements


```scala
// Add two elements
army += ("Helicopter" -> "Apache", "Missile" -> "Sidewinder")
```




    Map(Weapon -> M60, APC -> Bradley IFC, Missile -> Sidewinder, Tank -> A-1 Abrams, Aircraft -> F35, Helicopter -> Apache, Ship -> Nimitz Class)



## Remove An Element


```scala
// Remove an element
army -= "Ship"

// Remove an element (alternative)
army.remove("Tank")
```




    Some(A-1 Abrams)



## Change A Value


```scala
// Change the value of an element
army("Tank") = "Tiger Tank"
```

## Filter A Map


```scala
// Keep only the key, value pairs that meet the criteria
army.retain((k,v) => k == "Tank")
```




    Map(Tank -> Tiger Tank)


