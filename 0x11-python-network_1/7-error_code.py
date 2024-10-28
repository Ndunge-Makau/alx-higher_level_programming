#!/usr/bin/python3

"""Sends a request to the URL and displays the body of the response."""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        r = requests.get(url)
        print(r.text)
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e.status_code))
