#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don't need to check arguments passed to the script (number or type)
"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url).json()
    try:
        for i in range(0, 10):
            print(f"{response[i].get('sha')}: "
                  f"{response[i]['commit']['author']['name']}")
    except IndexError:
        pass
