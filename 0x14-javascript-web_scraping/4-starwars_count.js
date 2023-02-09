#!/usr/bin/node
// prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let times = 0;
    const data = JSON.parse(body).results;
    for (let i = 0; i < data.length; i++) {
      for (let j = 0; j < data[i].characters.length; j++) {
        if (data[i].characters[j].includes('/18/')) {
          times++;
          break;
        }
      }
    }
    console.log(times);
  }
});
