#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Get the file paths from the command-line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Read the content of the first file
const contentA = fs.readFileSync(fileA, 'utf8');

// Read the content of the second file
const contentB = fs.readFileSync(fileB, 'utf8');

// Concatenate the contents of both files
const concatenatedContent = contentA + contentB;

// Write the concatenated content to the destination file
fs.writeFileSync(fileC, concatenatedContent);

console.log('Concatenation successful!');
