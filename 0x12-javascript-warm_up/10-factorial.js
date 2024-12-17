#!/usr/bin/node
// Function to compute the factorial
function factorial (n) {
  // Base case: if n is 0 or 1, return 1
  if (n === 0 || n === 1) {
    return 1;
  }
  // Check if n is a valid number, if not return 1
  if (isNaN(n)) {
    return 1;
  }
  // Recursive case: n * factorial of (n-1)
  return n * factorial(n - 1);
}

// Convert the first argument to a number (argument passed to the script)
const num = parseInt(process.argv[2]);

// Compute and print the result
console.log(factorial(num));
