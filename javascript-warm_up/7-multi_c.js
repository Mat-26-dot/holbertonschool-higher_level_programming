#!/usr/bin/node
const arg = process.argv[2];
const x = parseInt(arg, 10);
if (isNaN(x)) {
    console.log('Missing number of occurences');
}   else if (x > 0) {
    const arr = [];
    for (let i = 0; i < x; i++) {
    arr.push('C is fun');
}
    console.log(arr.join('\n'));
}
