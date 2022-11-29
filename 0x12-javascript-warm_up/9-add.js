#!/usr/bin/node

const process = require('process');
const args = process.argv;

function add (a, b) {
  console.log(a + b);
}

const a = Number(args[2]);
const b = Number(args[3]);

if (!a || !b) {
  console.log(NaN);
} else {
  add(a, b);
}
