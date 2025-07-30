#!/usr/bin/node
function factorial(n) {
const num = parseInt(n)

if (isNaN(num)) {
  console.log(1);
  return 1;
}
    if (num <= 1) {
      return 1;
    }
    return num * factorial(num - 1);
}
const result = process.argv[2];

  console.log(result);

console.log(factorial(input));
