#!/usr/bin/python3
"""Function that appends a string at the end of
a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """script to append string in a text at the end"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
