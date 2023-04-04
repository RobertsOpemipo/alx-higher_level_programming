#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv
import sys

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
