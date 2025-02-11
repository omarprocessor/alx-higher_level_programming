#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  data.characters.forEach((character) => {
    request(character, (err, res, charBody) => {
      if (!err) {
        console.log(JSON.parse(charBody).name);
      }
    });
  });
});
