#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests

if __name__ == "__main__":
    CHAR = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": CHAR}

    res = requests.post("http://0.0.0.0:5000/search_user",
                        data=data, timeout=60)
    try:
        json = res.json()
        if json == {}:
            print("No result")
        else:
            print(f"[{json.get('id')}] {json.get('name')}")
    except ValueError:
        print("Not a valid JSON")
