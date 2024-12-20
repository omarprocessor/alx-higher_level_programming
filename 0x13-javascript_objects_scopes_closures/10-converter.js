#!/usr/bin/node
// Define the converter function
exports.converter = function (base) {
  return function (num) {
    if (num === 0) return '0'; // Special case for zero
    let result = '';
    while (num > 0) {
      const remainder = num % base;
      // Handle conversion for bases greater than 10 (e.g., hexadecimal)
      result = (remainder < 10 ? remainder : String.fromCharCode(remainder + 87)) + result;
      num = Math.floor(num / base);
    }
    return result;
  };
};
