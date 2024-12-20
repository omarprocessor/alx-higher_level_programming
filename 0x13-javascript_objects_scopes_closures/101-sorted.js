#!/usr/bin/node

// Import the dictionary from 101-data.js
const dict = require('./101-data').dict;

// Initialize a new dictionary to store user ids by occurrence
const newDict = {};

// Iterate over the original dictionary to populate the new dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // If this number of occurrences already exists as a key, add the userId to the list
  if (newDict[occurrences]) {
    newDict[occurrences].push(userId.toString());
  } else {
    // Otherwise, create a new list for this number of occurrences
    newDict[occurrences] = [userId.toString()];
  }
}

// Print the new dictionary
console.log(newDict);
