#!/usr/bin/node
// Get the list of arguments passed to the script
const args = process.argv.slice(2).map(arg => parseInt(arg));

// If there are less than two arguments, print 0
if (args.length < 2) {
  console.log(0);
} else {
  // Remove duplicates and sort in descending order
  const uniqueArgs = [...new Set(args)].sort((a, b) => b - a);

  // If there's a second element, print it; otherwise, print 0
  console.log(uniqueArgs[1] || 0);
}
