#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number of and the list of its arguments."""
    import sys

    count = len(sys.argv)
    if count == 1:
        print("0 arguments")
    elif count == 2:
        print("1 argument")
    else:
        print("{} argument:".format(count))
    for i in range(count):
        print("{} {}".format(i, sys.argv[i + 1]))
