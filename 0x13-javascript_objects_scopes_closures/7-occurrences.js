#!/usr/bin/node
const Square = require('./5-square');

class Square2 extends Square {
  charPrint (c) {
    const char = c || 'X'; // If c is not provided, default to 'X'
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width)); // Print the square using the character
    }
  }
}

module.exports = Square2;
