#!/usr/bin/node

const process = require('process');
const args = process.argv;

const number = Number(args[2]);
if (!number) {
  console.log('Missing number of occurances');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
