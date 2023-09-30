#!/usr/bin/python3
"""Displays the value of `X-Request-Id` header variable in the response.

Usage: ./5-hbtn_header.py <URL>
"""

import sys
import requests

req = requests.get(sys.argv[1], timeout=60)
print(req.headers.get("X-Request-Id"))
