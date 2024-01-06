#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count_args = len(sys.argv) - 1
    if count_args == 0:
        print("0 arguments.")
    else:
        print("{} arguments.".format(count_args))
    for count in range(count_args):
        print("{}: {}".format(count + 1, sys.argv[count + 1]))
