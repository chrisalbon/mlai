Title: Set Operations On Sequences   
Slug: set_operations_on_sequences       
Summary: Set Operations On Sequences Using Scala.  
Date: 2017-01-03 12:00  
Category: Scala  
Tags: Basics  
Authors: Chris Albon 

If you want to learn more, check out [Scala Cookbook](http://amzn.to/2lxbrxN) and [Programming in Scala](http://amzn.to/2lEtsLt).

## Preliminaries


```scala
import scala.collection.mutable.ArrayBuffer
```

## Create Two Array Sequences


```scala
// Create two arrays of ages
val student_ages = ArrayBuffer(42,25,28,38,58,63,23,458,2569,584,25,25)
val teacher_ages = ArrayBuffer(23,25,25,38,58,32,23,23,125,23,23,21,26)
```

## Concatenate Two Sequences


```scala
// Join two sequences end to end
student_ages ++ teacher_ages
```




    ArrayBuffer(42, 25, 28, 38, 58, 63, 23, 458, 2569, 584, 25, 25, 23, 25, 25, 38, 58, 32, 23, 23, 125, 23, 23, 21, 26)



## Intersection (Shared Elements) Of Two Sequences


```scala
// Create the interaction of two sequences
teacher_ages.intersect(student_ages)
```




    ArrayBuffer(23, 25, 25, 38, 58)



## Union (All Elements) Of Two Sequences


```scala
// Create the union of two sequences
teacher_ages.union(student_ages)
```




    ArrayBuffer(23, 25, 25, 38, 58, 32, 23, 23, 125, 23, 23, 21, 26, 42, 25, 28, 38, 58, 63, 23, 458, 2569, 584, 25, 25)



## Unique Elements In Union Of Two Sequences


```scala
// Create the union of two sequences then keep only the unique values
teacher_ages.union(student_ages).distinct
```




    ArrayBuffer(23, 25, 38, 58, 32, 125, 21, 26, 42, 28, 63, 458, 2569, 584)



## Relative Complement Of Two Sequences


```scala
// Elements in student_ages but not in teacher_ages
student_ages diff teacher_ages 
```




    ArrayBuffer(42, 28, 63, 458, 2569, 584, 25)


