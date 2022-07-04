#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry.py").BaseGeometry

class Rectangle:
    def __init__(self, width, height):
        self.__integer_validator("width", width)
        self.__width = width
        self.__integer_validator("height", height)
        self.__height = height
