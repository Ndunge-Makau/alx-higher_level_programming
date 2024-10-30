#!/usr/bin/env python3

"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/" + owner + '/' + repo + '/commits'

    try:
        response = requests.get(url).json()

        for i in range(10):
            print("{}: {}".format(response[i].get('sha'),
                                  response[i].get('commit').
                                  get('author').get('name')))

    except Exception as e:
        print(e)
