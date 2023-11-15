#!/usr/bin/node
const { argv } = require("node:process");
const args = argv.slice(2);
args.forEach((arg) => {
  const num = parseInt(arg);
  if (!isNaN(num)) {
    console.log('My number:' + num);
  }else{
  console.log('Not a number')}
});
