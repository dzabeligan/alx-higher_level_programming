#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1], timeout=60)
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
