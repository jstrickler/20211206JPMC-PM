"""
Geometric functions

<describe functions here>
"""
import math

PI = math.pi


def circle_area(diameter):
    """
    Calculate the area of a circle.

    :param diameter: Diameter of circle
    :return: Area of circle
    """
    radius = diameter / 2
    return math.pi * radius ** 2


def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    :param length: Length of long side
    :param width: Length of short side
    :return: Area of rectangle
    """
    return length * width
