#!/usr/bin/python3
"""Displays the value of `X-Request-Id` header variable in the response.

Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
