#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


res = requests.post(sys.argv[1], data={"email": sys.argv[2]}, timeout=60)
print(res.text)
