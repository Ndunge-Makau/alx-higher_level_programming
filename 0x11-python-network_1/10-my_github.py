#!/usr/bin/env python3

"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import sys
import requests

if __name__ == '__main__':
    url = "https://api.github.com/user"
    basic = (sys.argv[1], sys.argv[2])

    try:
        response = requests.get(url, auth=basic).json()
        print(response['id'])
    except Exception:
        print("None")
