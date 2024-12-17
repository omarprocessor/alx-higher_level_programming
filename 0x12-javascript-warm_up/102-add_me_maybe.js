#!/usr/bin/node
// Function that increments the number and calls the provided function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1); // Increment the number and pass it to theFunction
};
