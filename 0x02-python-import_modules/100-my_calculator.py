#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    count = len(sys.argv) - 1
    if count != 3:
        print("./100-my_calculator.py a operator b")
        sys.exit(1)
    Ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(Ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, Ops[sys.argv[2]](a, b)))

