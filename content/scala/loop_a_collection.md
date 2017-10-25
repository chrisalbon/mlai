Title: Loop A Collection   
Slug: loop_a_collection       
Summary: Loop A Collection Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create A Vector Collection


```scala
val vector = Vector("Male", 2, true)
```

## Loop Over The Collection


```scala
// For each item in the collection, print the class type of the element
vector.foreach((i: Any) => println(i, i.getClass.getSimpleName))
```

    (Male,String)
    (2,Integer)
    (true,Boolean)



```scala
// For each item in the collection
vector.foreach {
    // If one of these, print "Man"
    case "Male" | "M" | "Man" | "Gentleman" | "Boy" => println("Man")
    // For everything else, print "Something Else"
    case _ => println("Something Else")
}
```

    Man
    Something Else
    Something Else

