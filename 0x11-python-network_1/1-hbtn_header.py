#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable found in the header of the response."""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.headers['X-Request-Id'])
