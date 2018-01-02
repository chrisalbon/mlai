Title: Replacing Parts Of Strings  
Slug: replacing_parts_of_strings  
Summary: Replacing Parts Of Strings Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

This tutorial was inspired by the awesome [Scala Cookbook](http://amzn.to/2lxbrxN).

## Create A String


```scala
// Create a string value
val text: String = "Lt. Steve Miller will be leading the attack."
```

## Create A Regex Pattern


```scala
// Create a regex pattern for a name
val find_steve = "Steve Miller".r
```

## Replace Anything That Matches That Pattern With Something Else


```scala
// Replace all instances of the pattern with a different name
find_steve.replaceAllIn(text, "Peter Jackson")
```




    Lt. Peter Jackson will be leading the attack.



## Replace First Match


```scala
// Replace first instance of the pattern with a different name
find_steve.replaceFirstIn(text, "Peter Jackson")
```




    Lt. Peter Jackson will be leading the attack.


