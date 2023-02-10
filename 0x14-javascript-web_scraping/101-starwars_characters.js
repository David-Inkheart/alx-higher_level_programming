#!/usr/bin/node
// prints all characters of a Star Wars movie
// Display one character name by line in the same order of the list
// “characters” in the /films/ response

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    displayMovieStars(data, 0);
  }
});

function displayMovieStars (data, index) {
  request(data[index], function (error, response, body) {
    if (!error) {
      const movieStar = JSON.parse(body).name;
      console.log(movieStar);
      if (index + 1 < data.length) {
        displayMovieStars(data, index + 1);
      }
    }
  });
}
