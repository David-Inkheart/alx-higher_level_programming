#!/usr/bin/node
//  writes a string to a file

const fs = require('fs');
const str = process.argv[3];

fs.writeFile(process.argv[2], str, 'utf-8', function (err, str) {
  if (err) {
    console.log(err);
  }
});
