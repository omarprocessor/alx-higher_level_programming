#!/usr/bin/python3
"""
Script: 100-github_commits.py
Purpose:
    - Fetches the 10 most recent commits from a specified GitHub repository.
    - The script takes in two arguments: repository name and owner name.
    - It uses the GitHub API to get commits and prints them in
    the format <sha>: <author name>.
"""

import requests
import sys

if __name__ == "__main__":
    # Take repository name and owner name from command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API URL to fetch commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send a GET request to GitHub API
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        commits = response.json()

        # Loop over the first 10 commits and print the SHA and author name
        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author}")
    else:
        # If the request fails, print the error code
        print(f"Error: {response.status_code}")
