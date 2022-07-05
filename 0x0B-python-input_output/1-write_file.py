#!/usr/bin/python3
"""Function that write in a file"""


def write_file(filename="", text=""):
    """Script that write on a file in python."""

    with open(filename, "w", encoding="utf-_") as f:
        return f.write(text)
