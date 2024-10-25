#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    Usage: ./2-post_email.py <URL> <EMAIL>
"""

import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':

    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(values).encode("ascii")
    with urllib.request.urlopen(url) as response:
        print(response.read().decode("utf-8"))
