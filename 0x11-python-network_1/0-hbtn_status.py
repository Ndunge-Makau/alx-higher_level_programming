#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf')))
