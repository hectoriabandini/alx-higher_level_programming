const { argv } = require('node:process');

// Extract command-line arguments excluding the first two elements
const args = argv.slice(2);

// Check the number of arguments and print messages accordingly
if (args.length === 0) {
  console.log("No argument");
} else if (args.length === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
