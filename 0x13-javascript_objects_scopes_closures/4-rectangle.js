#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Initialize width and height if valid, otherwise create an empty object
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  // Method to print the rectangle using the character 'X'
  print () {
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // Method to rotate the rectangle (swap width and height)
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // Method to double the dimensions of the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
