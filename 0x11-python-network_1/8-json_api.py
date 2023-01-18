#!/usr/bin/python3
"""
Use requests package to make a post request to given URL with argument
set in variable `q`, defaulting to empty string. If response body is properly
JSON formatted and not empty, display `id` and `name` as given format.
Otherwise display error message.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    try:
        url = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url, data={"q": q}).json()

        if {'id', 'name'} <= r.keys():
            print('[{id}] {name}'.format(id=r.get('id'), name=r.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
