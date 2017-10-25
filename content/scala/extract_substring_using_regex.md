Title: Extract Substrings Using Regex  
Slug: extract_substring_using_regex  
Summary: Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

This tutorial was inspired by the awesome [Scala Cookbook](http://amzn.to/2lxbrxN).

## Create String


```scala
// Create a string value
val text: String = "27 aircraft"
```

## Create Regex Pattern


```scala
// Create a regex with two pattern matches (one number and one word)
val pattern = "([0-9]+) ([A-Za-z]+)".r
```

## Extract Substrings That Match Regex


```scala
// Apply the regex pattern such that each of the two pattern matches is assigned to a seperate value
val pattern(vehicle_number, vehicle_type) = text
```

## View Output


```scala
// View the value
vehicle_number
```




    27




```scala
// View the value
vehicle_type
```




    aircraft


