#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(arg => Number(arg));

if (numbers.length <= 1) {
  console.log(0);
}
// Initialize max and secondmax
let max = -Infinity;
let secondMax = -Infinity;
// Iterate through numbers to find max and secondMax
for (const num of numbers) {
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num < max && num > secondMax) {
    secondMax = num;
  }
}
// After iteration, print secondMax or 0 if it doesn't exist
if (secondMax === -Infinity) {
  console.log(0);
} else {
  console.log(secondMax);
}
