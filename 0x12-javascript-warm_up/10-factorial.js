#!/usr/bin/node

const process = require('process');
const args = process.argv;

function factorial (number) {
  if (number < 0) {
    return -1;
  } else if (number === 0) {
    return 1;
  } else {
    return (number * factorial(number - 1));
  }
}

const number = Number(args[2]);
if (!number) {
  console.log(1);
} else {
  console.log(factorial(number));
}
