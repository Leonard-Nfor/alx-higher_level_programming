#!/usr/bin/python3
"""direct the interpreter."""


class MyList(list):
    """A subclass of list that provides additional functionality.

    Methods:
        print_sorted(self): Print the list in ascending sorted order.

    Examples:
        >>> my_list = MyList([5, 3, 1, 4, 2])
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]

        >>> my_list = MyList([9, 6, 8, 7])
        >>> my_list.print_sorted()
        [6, 7, 8, 9]
        """

    def print_sorted(self):
        """Print the list in ascending sorted order.

        Returns:
            None

        Example:
            >>> my_list = MyList([5, 3, 1, 4, 2])
            >>> my_list.print_sorted()
            [1, 2, 3, 4, 5]
            """
        print(sorted(self))
