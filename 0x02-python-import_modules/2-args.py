#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("{} arguments.".format(0))
    elif len(sys.argv) == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        i = 1
        print("{} arguments:".format(len(sys.argv) - 1))
        while i < len(sys.argv):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
