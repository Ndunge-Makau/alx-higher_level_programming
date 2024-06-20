#!/usr/bin/node

let end = process.argv.length - 1;
let myArray = process.argv.slice(2, end);

myArray.sort((a, b) => a - b).reverse();
if (myArray.length == 0 || myArray.length == 1) {
  console.log(0);
} else {
  console.log(myArray[1]);
}
