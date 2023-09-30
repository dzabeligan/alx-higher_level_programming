#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
from urllib import parse, request


if __name__ == "__main__":
    req = request.Request(sys.argv[1], parse.urlencode({
        "email": sys.argv[2]}).encode("ascii"))
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
