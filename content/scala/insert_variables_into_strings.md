Title: Insert Variables Into Strings
Slug: insert_variables_into_strings  
Summary: Insert Variables Into Strings Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want a deeper guide to Scala, when I was learning I used [Programming Scala](http://amzn.to/2lV1Ioz) and [Scala for Data Science](http://amzn.to/2mG99OG).

The proper term from this is _string interpolation_.

## Create A Value


```scala
// Create some values
val number_of_soldiers: Short = 542
val casualties: Short = 32
```

## Add The Value To A String


```scala
print(f"Before the battle we had $number_of_soldiers soldiers. However, now we have ${number_of_soldiers - casualties}.")
```

    Before the battle we had 542 soldiers. However, now we have 510.
