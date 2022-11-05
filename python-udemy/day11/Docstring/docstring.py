import mypy
import sys
import os
import re

class Animal:
    def __init__(self, name, weight, height):
        """

        :param name:
        :param weight:
        :param height:
        """
        self.name = name
        self.weight = weight
        self.height = height

def soma(x,y):
    """

    :param x: an int number
    :param y: other int number
    :return: the result of sum of x and y
    """
    return x+y


help(classmethod)