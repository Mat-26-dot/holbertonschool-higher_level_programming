#!/usr/bin/node
const args = process.argv.slice(2);

const numbers = args.map(arg => Number(arg)); // convert all to integers
// created var and assigned to convert into int by using parseInt and argvWrite a script that searches the second biggest integer in the list of arguments.
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


//You can assume all arguments can be converted to integer
//If no argument passed, print 0
//If the number of arguments is 1, print 0
//You must use console.log(...) to print all output
//You are not allowed to use var