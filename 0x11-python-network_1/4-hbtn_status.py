#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status", timeout=60)
    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
