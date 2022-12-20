#!/usr/bin/node

const args = parseInt(process.argv[2]);
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < args; idx++) { console.log('C is fun'); }
}
