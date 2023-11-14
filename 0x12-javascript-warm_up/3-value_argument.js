#!/usr/bin/node
const { argv } = require('node:process');

// Extract command-line arguments excluding the first two elements
const args = argv.slice(2);

// Check if any arguments are present and print the first one or "No argument"
console.log(args[0] !== undefined ? args[0] : "No argument");
