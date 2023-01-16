#!/bin/bash
# sending GET request and displaying body of 200 status code response
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
