#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests

if __name__ == "__main__":
    r = requests.get(
        f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}"
        "/commits", timeout=60)

    commits = r.json()
    try:
        for i in range(10):
            print(
                f"{commits[i].get('sha')}: "
                f"{commits[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
