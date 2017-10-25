Title: For Looping   
Slug: for_looping       
Summary: For Loops Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

This tutorial was inspired by the awesome [Scala Cookbook](http://amzn.to/2lxbrxN).

## Create An Array


```scala
val staffMembers = Array("Jason Miller", "Steve Miller", "Sally Fields")
```

## Loop Over Every Item In The Array


```scala
// Create a value that is the output, then for each person in staff
val staffFirstNames = for (person <- staffMembers) yield {
                        // Upper case the name
                        val upperCaseFullNames = person.toUpperCase
                        // Get the first name by splitting the full name by space and taking the first element
                        val firstName = upperCaseFullNames.split(" ")(0)
                        // Return the first name
                        firstName
                      }
```


```scala
// View the returned values
staffFirstNames
```




    Array(JASON, STEVE, SALLY)



## Loop Over Every Item In The Array That Meets A Criteria

An if statement in a for loop is called a "guard."


```scala
// Create a value that is the output, then for each person in staff with the last name of Miller
val staffWithLastNameMiller = for (person <- staffMembers if person.split(" ")(1) == "Miller") yield {
                                // Get the first name by splitting the full name by space and taking the first element
                                val firstName = person.split(" ")(0)
                                // Return the first name
                                firstName
                              }
```


```scala
// View the returned values
staffWithLastNameMiller
```




    Array(Jason, Steve)



## Loop With Value And Index

This is like Python's `enumerate()`.


```scala
// Create a value that is the output, then for each person and index, yield
val staffNamesAndIndex = for ((person, i) <- staffMembers.zipWithIndex) yield {
                           // Upper case the name
                           val firstName = person.split(" ")(0)
                           // Return a tuple with the first name and index
                          (firstName, i)
                         }
```


```scala
// View the returned values
staffNamesAndIndex
```




    Array((Jason,0), (Steve,1), (Sally,2))


