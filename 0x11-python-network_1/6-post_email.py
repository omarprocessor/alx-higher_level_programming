#!/usr/bin/python3
"""
Script: 6-post_email.py
Purpose:
    - Sends a POST request to the passed URL with the email as a parameter.
    - Displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Define the email data to be sent in the POST request
    data = {'email': email}

    # Send POST request
    response = requests.post(url, data=data)

    # Display the body of the response
    print("Your email is:", email)
    print(response.text)
