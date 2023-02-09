#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i++) {
      request(data[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const movieStar = JSON.parse(body).name;
          console.log(movieStar);
        }
      });
    }
  }
});
