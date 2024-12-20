#!/usr/bin/node
// Initialize a counter to track the number of arguments printed
let count = 0;

// Define the logMe function
exports.logMe = function (item) {
  console.log(`${count}: ${item}`); // Print the current count and the item
  count++; // Increment the counter after printing
};
