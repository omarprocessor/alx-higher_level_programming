#!/bin/bash
# Send a GET request to the URL and output only the HTTP status code
curl -o /dev/null -s -w "%{http_code}" "$1"

