#!/usr/bin/node
const arg = process.argv[2];
const x = parseInt(arg, 10);
if (isNaN(x)) {
    console.log('Missing number of occurences');
} else {
let output = '';
for (let i = 0; i < x; i++) {
  output += 'C is fun\n';
}
console.log(output);
}
