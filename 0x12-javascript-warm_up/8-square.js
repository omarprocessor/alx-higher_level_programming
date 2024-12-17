#!/usr/bin/node
const args = process.argv;
let size = args[2];
if (isNaN(Number(size))) {
  console.log('Missing size');
} else {
for (let i = 0; i < size; i++){
  let row = '';
  for (let j = 0; j < size; j++) {
    row += 'X';
  }
  console.log(row);
}
}
