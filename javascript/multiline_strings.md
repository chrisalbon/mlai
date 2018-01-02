Title: Multiline Strings
Slug: multiline_strings
Summary: Multiline Strings In Javascript
Date: 2016-03-15 12:00
Category: Javascript
Tags: Basics
Authors: Chris Albon

There are various ways to include multiline strings in JavaScript. Here is the generally preferable way.

```javascript
// Create a series of strings, one per desired line.
var multiline = "Hello Steve\n" +
                  "Rock on.\n" +     
                  "From Chris";


// Print the string
console.log(multiline)
```

    Hello Steve
    Rock on.
    From Chris
