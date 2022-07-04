#!/usr/bin/python3

Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.__intger_validator("size", size)
        super().__init__(size, size)
        self.__size = size
