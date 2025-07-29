#!/usr/bin/node
const arg = process.argv[2];

if (arg && /^-?\d+$/.test(arg)) {
  const num = parseInt(arg, 10);
  console.log('My number:', num);
} else {
  console.log('Not a number');
}