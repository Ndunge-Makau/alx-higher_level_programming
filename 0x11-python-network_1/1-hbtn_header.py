#!/usr/bin/python3

"""Sends a request to the URL and displays the value of the X-Request-Id"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.headers['X-Request-Id'])
