#!/usr/bin/python3
"""
Script: 0-hbtn_status.py
Purpose:
    - Fetches the URL `https://alx-intranet.hbtn.io/status`
    using the `urllib` package.

    - Displays the response body in a specific format:
        Body response:
            - type: <class 'bytes'>
            - content: b'OK'
            - utf8 content: OK

Requirements:
    - Must use the `urllib` package.
    - Cannot import any other Python libraries.
    - Must use a `with` statement to handle the HTTP response.
    - Output must match the exact format shown in the usage example.

Usage:
    1. Save this script as `0-hbtn_status.py`.
    2. Make it executable with `chmod +x 0-hbtn_status.py`.
    3. Execute the script:
        ./0-hbtn_status.py

Example:
    guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
    Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
    guillaume@ubuntu:~/0x11$

GitHub Repository:
    alx-higher_level_programming
Directory:
    0x11-python-network_1
File:
    0-hbtn_status.py
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
