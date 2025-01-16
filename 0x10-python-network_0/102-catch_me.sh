#!/bin/bash
# Sends a POST request to 0.0.0.0:5000/catch_me to get the response containing "You got me!"
curl -sL -X POST 0.0.0.0:5000/catch_me
