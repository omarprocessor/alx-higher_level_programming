#!/usr/bin/python3
"""
Script: 1-hbtn_header.py
Purpose:
    - Takes a URL as input from the command line.
    - Sends a request to the URL.
    - Displays the value of the `X-Request-Id` variable from
    the response header.

Requirements:
    - Use `urllib` and `sys` modules.
    - No other modules are allowed.
    - Use a `with` statement to handle the HTTP response.

Usage:
    ./1-hbtn_header.py <URL>

Example:
    guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
    ade2627e-41dd-4c34-b9d9-a0fa0f47b237
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get URL from command line arguments

    # Send the request and read the response
    with urllib.request.urlopen(url) as response:
        # Get the X-Request-Id from the headers
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
