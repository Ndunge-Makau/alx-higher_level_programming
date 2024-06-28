#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}

if (Number.isInteger(first) && Number.isInteger(second)) {
  console.log(add(first, second));
} else {
  console.log('NaN');
}
