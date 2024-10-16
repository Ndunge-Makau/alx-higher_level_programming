#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -sLI $1 | grep Allow: | awk '{for (i=2; i<= NF; i++) {printf $i; if (i < NF) printf " ";} printf "\n"}'
