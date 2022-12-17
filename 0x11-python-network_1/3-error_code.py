#!/usr/bin/python3
"""
Python script that takes in a URL
sends a request to the URL and displays the body of the response.
manage urllib.error.HTTPError exceptions and print: Error code: {error code}
"""
import sys
from urllib import request
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("UTF-8"))
    except HTTPError as ex:
        print("Error code:", ex.code)
