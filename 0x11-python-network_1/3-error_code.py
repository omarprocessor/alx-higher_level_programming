#!/usr/bin/python3
"""
Script: 3-error_code.py
Purpose:
    - Takes a URL as input from the command line.
    - Sends a request to the URL.
    - Displays the body of the response (decoded in UTF-8).
    - Handles `urllib.error.HTTPError` exceptions and prints
    the HTTP status code.

Requirements:
    - Use `urllib` and `sys` modules only.
    - Use a `with` statement to handle the HTTP response.

Usage:
    ./3-error_code.py <URL>

Example:
    guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
    Index
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
