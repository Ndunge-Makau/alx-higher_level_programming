#!/bin/bash
# Causes the server to respond with a message containing You got me!, in the body of the response.
curl -sL -X PUT -H "Content-Type: application/x-www-form-urlencoded" -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me_2
