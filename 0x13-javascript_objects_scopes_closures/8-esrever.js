#!/usr/bin/node
// Define the esrever function to reverse the list without using the built-in reverse method
exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
