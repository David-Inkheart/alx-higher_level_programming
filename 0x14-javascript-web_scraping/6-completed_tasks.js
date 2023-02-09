#!/usr/bin/node
// computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const compTasks = {};
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (!(data[i].userId in compTasks)) {
          compTasks[data[i].userId] = 0;
        }
        compTasks[data[i].userId] += 1;
      }
    }
    console.log(compTasks);
  }
});
