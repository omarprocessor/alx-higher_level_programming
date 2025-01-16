#!/bin/bash
# Send a POST request with the contents of a file as JSON data and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
