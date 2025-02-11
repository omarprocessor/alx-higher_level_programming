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
  const characters = data.characters;
  fetchCharacters(characters, 0);
});

function fetchCharacters (characters, index) {
  if (index >= characters.length) return;
  request(characters[index], (err, res, charBody) => {
    if (!err) {
      console.log(JSON.parse(charBody).name);
      fetchCharacters(characters, index + 1);
    }
  });
}
