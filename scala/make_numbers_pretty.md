Title: Make Numbers Pretty   
Slug: make_numbers_pretty  
Summary: Make Numbers Pretty Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

This tutorial was inspired by the awesome [Scala Cookbook](http://amzn.to/2lxbrxN).

## Load The NumberFormat Library


```scala
// Make value that is assigned to an instance of numberformat
val make_pretty = java.text.NumberFormat.getInstance
```

## Make An Integer Pretty


```scala
// Format 10000 to 10,000
make_pretty.format(10000)
```

## Make A Float Pretty


```scala
// Format to 10000.1928 to 10,000.193
make_pretty.format(10000.1928)
```




    10,000.193



## Load The NumberFortmat Library Set For European Numbers


```scala
// Set the locale to germany
val germany = new java.util.Locale("de", "DE")

// Make value that is assigned to an instance of numberformat set to germany
val make_pretty_de = java.text.NumberFormat.getIntegerInstance(germany)
```

## Make An Integer Pretty


```scala
// Format 1000000 to 1.000.000
make_pretty_de.format(1000000)
```




    1.000.000


