#!/usr/bin/python3
"""
Script: 2-post_email.py
Purpose:
    - Takes a URL and an email address as command-line arguments.
    - Sends a POST request to the URL with the email as a parameter.
    - Displays the response body, decoded in UTF-8.

Requirements:
    - Use `urllib` and `sys` modules only.
    - Email must be sent as the `email` variable.
    - Use a `with` statement to handle the HTTP response.

Usage:
    ./2-post_email.py <URL> <email>

Example:
    guillaume@ubuntu:~/0x11$ ./2-post_email.py
    http://0.0.0.0:5000/post_email hr@holbertonschool.com
    Your email is: hr@holbertonschool.com
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get URL from command-line arguments
    email = sys.argv[2]  # Get email from command-line arguments

    # Prepare the data for POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request
    with urllib.request.urlopen(url, data) as response:
        # Decode and print the response body
        print(response.read().decode('utf-8'))
