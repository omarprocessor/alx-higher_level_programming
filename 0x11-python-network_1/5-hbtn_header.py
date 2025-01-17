#!/usr/bin/python3
"""
Script: 5-hbtn_header.py
Purpose:
    - Sends a request to a given URL and displays the
    value of the 'X-Request-Id'
      variable found in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send GET request
    response = requests.get(url)

    # Display the value of X-Request-Id in the header
    print(response.headers.get('X-Request-Id'))
