#!/usr/bin/python3
"""
Script: 4-hbtn_status.py
Purpose:
    - Fetches https://alx-intranet.hbtn.io/status using the requests package.
    - Displays the type, content, and utf-8 decoded
    content of the response body.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Send GET request
    response = requests.get(url)

    # Display the response details
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
    print(f"\t- utf8 content: {response.text.encode('utf-8')}")
