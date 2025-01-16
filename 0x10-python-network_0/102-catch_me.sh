#!/bin/bash
# Script that makes the server respond with "You got me!"
curl -sL -X GET 0.0.0.0:5000/catch_me
