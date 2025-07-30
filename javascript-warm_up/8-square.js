#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
    }
}
//The script gets the size from the command line.

//If no valid size is provided, prints an error. (Missing size)

//Otherwise, prints a square of X's, using a for-loop,
// with sides equal to the given size.