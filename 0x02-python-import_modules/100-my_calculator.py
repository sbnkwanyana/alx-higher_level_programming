#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import div, mul, sub, add
    import sys
    operators = ['+', '-', '*', '/']
    error_message1 = "Usage: {} <a> <operator> <b>".format(sys.argv[0])
    error_message2 = "Unknown operator. Available operators: +, -, * and /"
    if len(sys.argv) != 4:
        print(error_message1)
        sys.exit(1)
    else:
        if sys.argv[2] not in operators:
            print(error_message2)
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == operators[0]:
                print(f"{a} + {b} = {add(a, b)}")
            elif sys.argv[2] == operators[1]:
                print(f"{a} - {b} = {sub(a, b)}")
            elif sys.argv[2] == operators[2]:
                print(f"{a} * {b} = {mul(a, b)}")
            elif sys.argv[2] == operators[3]:
                print(f"{a} / {b} = {div(a, b)}")
        sys.exit(0)
