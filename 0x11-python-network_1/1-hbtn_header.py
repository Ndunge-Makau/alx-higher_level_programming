#!/usr/bin/python3
""" Sends a request to the URL and displays the value of the X-Request-Id
Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
