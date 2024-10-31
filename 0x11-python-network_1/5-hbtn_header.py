#!/usr/bin/env python3

"""Sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
