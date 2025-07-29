#!/usr/bin/node
const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';
for (let i = 0; i < lines.length; i++) {
  output += lines[i] + (i === lines.length - 1 ? '' : '\n');
}
console.log(output);

Explanation
// We store all lines in an array.

// We loop over the array and build a string with each line.

// We add a newline after each line except the last one (using ternary operator).

//We print all lines at once using a single console.log.