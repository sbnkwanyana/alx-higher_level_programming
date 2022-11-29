#!/usr/bin/node

const process = require('process');
const args = process.argv;

let arg = args[2];
if (!arg)
{
    console.log('No argument');
}
else
{
    console.log(arg);
}
