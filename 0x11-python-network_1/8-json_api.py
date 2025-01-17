#!/usr/bin/python3
"""
Script: 8-json_api.py
Purpose:
    - Sends a POST request to http://0.0.0.0:5000/search_user with
    the letter as a parameter.
    - Displays the result in a specific format based on the response.
"""

import requests
import sys

if __name__ == "__main__":
    # If no argument is passed, set q to ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the payload for the POST request
    payload = {'q': q}

    # Send POST request to the given URL
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        # Check if the JSON response is empty
        if not json_response:
            print("No result")
        else:
            # Display the id and name from the JSON response
            print(f"[{json_response['id']}] {json_response['name']}")
    except ValueError:
        # Handle invalid JSON format
        print("Not a valid JSON")
