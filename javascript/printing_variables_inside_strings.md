Title: Printing Variables Inside Strings
Slug: printing_variables_inside_strings
Summary: Printing Variables Inside Strings
Date: 2016-03-15 12:00
Category: Javascript
Tags: Basics
Authors: Chris Albon

String formatting in JavaScript works very similar to other languages like Python 3. String concatenation allows for non-string variables to be incorporated into string variables.

There are two basic ways of printing variables inside strings. Here is the first:

```javascript
// Create a variable called currentTemp
let votingTime = 3;

// Create a constant (variable) with a string that includes the value from currentTemp
const message = "Voters should go to polling station at " + votingTime + "pm";

// Print the string
console.log(message)
```
    Voters should go to polling station at 3pm

In the first way, you simply wrap the variable in strings. There is, however, a more modern way of achieving the same output:

```javascript
// Create a constant (variable) with a string that includes the value from currentTemp
const message = `Voters should go to polling station at ${votingTime}pm`;

// Print the string
console.log(message)
```

    Voters should go to polling station at 3pm

In the example above, instead of wrapping the variable in strings, we called the variable directly from inside a string.
