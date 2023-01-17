#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)"""

from sys import argv
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_info = response.read()
        print(the_info.decode('utf-8'))
