#!/usr/bin/python3
"""Direct the interpreter"""


def inherits_from(obj, a_class):
    """check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    type(obj) != a_class check if obj is not thesame as a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
