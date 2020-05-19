#!/usr/bin/python3
""" Contains a class to create a square """


class square():
    """ Create a square """

    def __init__(self, width, height):
        """ Set square attributes """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter of a Square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String version of a square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square if this file was executed """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
