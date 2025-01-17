#!/usr/bin/python3
"""
Script: 7-error_code.py
Purpose:
    - Sends a request to the passed URL.
    - Displays the body of the response.
    - If the HTTP status code is greater than or equal to 400,
      it prints "Error code:" followed by the value of the status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send GET request
        response = requests.get(url)

        # Check if the status code is greater than or equal to 400
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)

    except requests.exceptions.RequestException as e:
        # Catch exceptions and print error code
        print(f"Error code: {e}")
