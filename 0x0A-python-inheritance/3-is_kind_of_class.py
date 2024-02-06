#!/usr/bin/python3
""" direct the interpreter"""


def is_kind_of_class(obj, a_class):
    """check object's types"""
    if isinstance(obj, a_class):
        return True
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
