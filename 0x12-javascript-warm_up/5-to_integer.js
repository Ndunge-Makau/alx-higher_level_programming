#!/usr/bin/node

const argv = process.argv;
const number = parseInt(argv[2]);

if (Number.isInteger(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a Number');
}
