#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const tasks = JSON.parse(body).filter(task => task.completed);
    const result = {};
    tasks.forEach(task => {
      result[task.userId] = (result[task.userId] || 0) + 1;
    });
    console.log(result);
  }
});
