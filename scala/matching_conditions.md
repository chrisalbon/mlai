Title: Matching Conditions   
Slug: matching_conditions       
Summary: Matching Conditions Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Create A String


```scala
// Create some strings
val text1 = "Man"
val text2 = "F"
val text3 = "Dog"
```

## Create A Function That Uses A Match Expression


```scala
// Define a function that takes in a string, and matches it
def findGender(word: String) = word match {
    // If any of these words, return "Woman"
    case "Female" | "F" | "Woman" | "Lady" | "Girl" => "Woman"
    // If any of these words, return "Man"
    case "Male" | "M" | "Man" | "Gentleman" | "Boy" => "Man"
    // If anything else, return "Unknown"
    case _ => "Unknown"
}
```

## Apply The Function To The Strings


```scala
findGender(text1)
```




    Man




```scala
findGender(text2)
```




    Woman




```scala
findGender(text3)
```




    Unknown


