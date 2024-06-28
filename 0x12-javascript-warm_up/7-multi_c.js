#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
