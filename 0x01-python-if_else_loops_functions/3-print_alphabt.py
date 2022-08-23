#!/usr/bin/python3
for c in (chr(i) for i in range(97, 123)):
    if c != 'q' and c != 'e':
        print("{0}".format(c), end="")
