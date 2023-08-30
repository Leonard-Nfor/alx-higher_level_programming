#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list

    Args:
        my_list(list): The list to print elements from
        x(int): Number of elements of my_list

    Returns:
        The number of elements pointed
    """
    j = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            j += 1
        except indexError:
            break
        print("")
        return(j)
