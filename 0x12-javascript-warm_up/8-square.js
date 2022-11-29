#!/usr/bin/node

const process = require('process');
const args = process.argv;

const size = Number(args[2]);
if (!size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let j;
    for (j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    j = 0;
    console.log();
  }
}
