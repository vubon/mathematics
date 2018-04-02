"""
Created at : 02-04-2018
Author: Vubon Roy

"""

pi = 3.141592653589793


def addition(x, y):
    """
    sum of two real number
    :param x:
    :param y:
    :return: total of x and y value
    """
    return x + y


def subtraction(x, y):
    """
    Two real numbers subtract
    :param x:
    :param y:
    :return: return the value of x - y
    """
    return x - y


def multiplication(x, y):
    """

    :param x:
    :param y:
    :return: multiply x and y values
    """
    return x * y


def division(x, y):
    """
    Division both real numbers
    :param x:
    :param y:
    :return:
    """

    if y == 0:
        raise ValueError("Divisor can't 0")
    return x / y


def sqrt(x):
    """
    sqrt(x)
    :type x: real number
    :return float.
    """

    return "{0:.3f}".format(x ** 0.5)


def power(x):
    """
    power of the x
    :type x: real.numbers
    :param x:
    :return: float
    """
    return "{0:.3f}".format(x ** 2)


def cube(x):
    """

    :param x:
    :return:
    """
    return x ** 3


def circle_area(radius):
    """
    :type: numbers.real
    :param radius:
    :rtype: float
    """

    return "{0:.3f}".format(2*pi*radius**2)


def circumference(radius):
    """
    :type: real.numbers
    :param: radius
    :rtype: float
    """
    return "{0:.3f}".format(2*pi*radius)