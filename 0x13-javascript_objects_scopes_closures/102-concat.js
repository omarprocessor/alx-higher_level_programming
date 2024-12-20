#!/usr/bin/node
const fs = require('fs');

// Read the contents of the first file
const fileContent1 = fs.readFileSync(process.argv[2], 'utf8');

// Read the contents of the second file
const fileContent2 = fs.readFileSync(process.argv[3], 'utf8');

// Write the concatenated contents into the destination file
fs.writeFileSync(process.argv[4], fileContent1 + fileContent2);
