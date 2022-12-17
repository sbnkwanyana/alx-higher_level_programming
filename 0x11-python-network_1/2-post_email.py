#!/usr/bin/python3
"""
Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode("UTF-8")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("UTF-8"))
