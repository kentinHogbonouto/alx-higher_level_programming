#!/usr/bin/python3

def inherits_from(obj, a_class):
    if issubclass(obj, a_class):
        return True
    return False
