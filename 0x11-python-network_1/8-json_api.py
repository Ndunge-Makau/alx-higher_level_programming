#!/usr/bin/python3

"""Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import sys
import requests

if __name__ == '__main__':

    if len(sys.argv) == 1:
        payload = {'q': ''}
    else:
        payload = {'q': sys.argv[1]}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        rj = r.json()
        if rj == {}:
            print("No result")
        else:
            print("[{}] {}".format(rj['id'], rj['name']))
    except ValueError:
        print("Not a valid JSON")
