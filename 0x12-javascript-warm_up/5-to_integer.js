#!/usr/bin/node
const args = process.argv;
const f = args[2];
if (isNaN(Number(f))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${f}`);
}
