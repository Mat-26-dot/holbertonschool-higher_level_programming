#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}
const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);

add(a, b);
