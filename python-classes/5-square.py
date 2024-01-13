#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that defines a square:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0)"""
    def __init__(self, size=0):
        """Size is a private attribute :
            - size must be an integer, otherwise raise a TypeError exception
              with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with the
              message size must be >= 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """size Property"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """setter for size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method:
           Return: the current square area"""
        return(self.__size * self.__size)

    def my_print(self):
        """Prints the square with the character #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                    print("#" * self.size)
