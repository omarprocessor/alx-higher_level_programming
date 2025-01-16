#!/bin/bash
# Sends a POST request to 0.0.0.0:5000/catch_me to get the response containing "You got me!"
curl -s http://0.0.0.0:5000/catch_me | grep -q "You got me!" && echo "Success!" || :
