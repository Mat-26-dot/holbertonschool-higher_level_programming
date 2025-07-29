#!/usr/bin/node
const lines = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let output = '';
for (let i = 0; i < lines.length; i++) {
    output += lines[i] + (i === lines.length - 1 ? '' : '\n');
}
console.log(output);
