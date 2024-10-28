#!/usr/bin/env python3

"""Fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == '__main__':
      request = requests.get("https://alx-intranet.hbtn.io/status").text

      print("Body response:")
      print("\t- type: {}".format(type(request)))
      print("\t- content: {}".format(request))
