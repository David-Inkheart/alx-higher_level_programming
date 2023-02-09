#!/usr/bin/node
// read a file, store its contents in a variable
// then log its contents to the console

const fs = require('fs');

function readFile (filePath) {
  fs.readFile(filePath, 'utf-8', function (err, data) {
    if (!err) {
      console.log(data.toString());
    } else {
      console.log(err);
    }
  });
}
readFile(process.argv[2]);
