#!/usr/bin/node
// Function that calls 'theFunction' 'x' times
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction(); // Calls the function each time
  }
};
