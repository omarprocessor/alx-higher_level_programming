#!/usr/bin/python3
"""
Script: 10-my_github.py
Purpose:
    - Uses GitHub API with Basic Authentication to fetch the user ID.
    - Takes GitHub username and personal access token as
    password from command-line arguments.
"""

import requests
import sys

if __name__ == "__main__":
    # Take the username and personal access token from
    # the command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # URL to access the GitHub user info API
    url = "https://api.github.com/user"

    # Send a GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Check if the response was successful
    if response.status_code == 200:
        # Print the user ID from the response JSON
        print(response.json().get('id'))
    else:
        # If authentication failed, print None
        print(None)
