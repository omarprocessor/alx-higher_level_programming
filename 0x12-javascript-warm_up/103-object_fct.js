#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value += 1; // Increment the 'value' property
  }
};

console.log(myObject);

// Call the incr function to increment 'value'
myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
