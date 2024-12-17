#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value += 1; // Increments the 'value' property by 1
  }
};

console.log(myObject); // First log, without 'incr' function showing yet

myObject.incr(); // Call the incr function
console.log(myObject); // After first increment

myObject.incr(); // Call the incr function again
console.log(myObject); // After second increment

myObject.incr(); // Call the incr function once more
console.log(myObject); // After third increment
