#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the Rectangle constructor with both width and height set to size
  }
}

module.exports = Square;
