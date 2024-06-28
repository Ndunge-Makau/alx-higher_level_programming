#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    let myXs = '';
    for (let j = 0; j < number; j++) {
      myXs += 'X';
    }
    console.log(myXs);
  }
} else {
  console.log('Missing size');
}
