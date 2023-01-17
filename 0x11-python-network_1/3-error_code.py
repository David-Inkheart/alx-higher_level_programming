#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
and displays the body of the response (decoded in utf-8)
manage urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code"""

from sys import argv
import urllib.parse
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            info = response.read()
            print(info.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
