#!/usr/bin/python3

"""Sends a POST request to the passed URL
with the email as a parameter,
and finally displays the body of the response."""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    r = requests.post(url, data)
    print(r.text)
