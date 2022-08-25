#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for value in dir(hidden_4):
        if value[0] == "_" and value[1] == "_":
            continue
        print("{}".format(value))
