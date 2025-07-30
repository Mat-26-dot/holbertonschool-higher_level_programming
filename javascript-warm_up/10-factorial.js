#!/usr/bin/node
const firstarg = process.argv[2];
const num = Number(firstarg);

if (isNaN(num)) {
  console.log(1);
  process.exit();
}
  const n = Math.floor(num);

  const factorial = (x) => {
    if (x <= 1) {
      return 1;
    }
    return x * factorial(x - 1);
  };
  const result = factorial(n);

  console.log(result);