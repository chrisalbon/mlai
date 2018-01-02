Title: Try, Catch, Finally   
Slug: try_catch_finally       
Summary: Try, Catch, Finally Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create Some Operation That Will Cause An Exception


```scala
"Sixteen".toFloat
```




    Name: java.lang.NumberFormatException
    Message: For input string: "Sixteen"
    StackTrace:   at sun.misc.FloatingDecimal.readJavaFormatString(FloatingDecimal.java:2043)
      at sun.misc.FloatingDecimal.parseFloat(FloatingDecimal.java:122)
      at java.lang.Float.parseFloat(Float.java:451)
      at scala.collection.immutable.StringLike$class.toFloat(StringLike.scala:280)
      at scala.collection.immutable.StringOps.toFloat(StringOps.scala:29)



## Try, Catch, Finally


```scala
// Try
try {
    // The bad operation
    "Sixteen".toFloat
// Catch any problems
} catch {
    // If it is an exception, print something
    case e: Exception => println("Something went wrong")
} finally {
    // Regardless of if there is an error or not, print this
    println("We are finally done.")
}
```

    Something went wrong
    We are finally done.





    ()


