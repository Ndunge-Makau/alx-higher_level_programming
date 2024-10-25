#!/usr/bin/python3
"""
Sends an HTTP request to the provided URL and displays the value of the 'X-Request-Id' 
header from the server's response.

Usage:
    ./script.py <URL>

Parameters:
    <URL>: The URL to which the HTTP request is sent.

Output:
    Prints the value of the 'X-Request-Id' header from the HTTP response.

Example:
    $ ./script.py http://example.com
    12345-abcdef

Raises:
    urllib.error.URLError: If there is an issue with the network or the URL is invalid.
    urllib.error.HTTPError: If the server returns an HTTP error code.
"""


import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
