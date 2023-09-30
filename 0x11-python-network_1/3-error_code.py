#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
from urllib import error, request


req = request.Request(sys.argv[1])
try:
    with request.urlopen(req) as response:
        print(response.read().decode("ascii"))
except error.HTTPError as e:
    print(f"Error code: {e.code}")
