Title: Search Strings  
Slug: search_strings  
Summary: Search Strings Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want a deeper guide to Scala, when I was learning I used [Programming Scala](http://amzn.to/2lV1Ioz) and [Scala for Data Science](http://amzn.to/2mG99OG).

## Create A String


```scala
// Create a value called text that is a string
val text: String = "This is a sentence that we want to split along every space"
```




    Array(This, is, a, sentence, that, we, want, to, split, along, every, space)



## Split Up A String By Commas


```scala
// Create a value called csv_row that is a string and contains one row of data
val csv_row: String = "Billy, Miller, 22, Baker, High School"

// Split up that row by commas
csv_row.split(",")
```




    Array(Billy, " Miller", " 22", " Baker", " High School")


