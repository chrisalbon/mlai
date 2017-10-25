Title: Search Strings Using Regex  
Slug: search_strings_with_regex  
Summary: Search Strings Using Regex Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

This tutorial was inspired by the awesome [Scala Cookbook](http://amzn.to/2lxbrxN).

## Create A String


```scala
// Create a string value
val attack_order : String = "Our 382 troops will attack their east flank at dawn. They have 28 troops there."
```

## Create A Regex Pattern


```scala
// Create a value that is a regex pattern
val find_numbers = "[0-9]+".r
```

## Find First Match


```scala
// Apply the regex to find the first match, output the result, otherwise output "None"
find_numbers.findFirstIn(attack_order).getOrElse("None")
```




    382



## Find All Matches


```scala
// Apply the regex to find all matches and output to an array
find_numbers.findAllIn(attack_order).toArray
```




    Array(382, 28)


