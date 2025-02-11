#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const count = JSON.parse(body).results.filter(film =>
      film.characters.some(char => char.includes('/18/'))
    ).length;
    console.log(count);
  }
});
