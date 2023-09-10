#!/usr/bin/env python
"""
Cell class definition
"""
import numpy as np


class Cell():
    """
    Base functionality for a cell in multi-dimensional space.
    """

    def __init__(self, centre = [0,0], size = 1., dimension = 2, active = True):
        """
        Initialise cell and calculate correct dimension.

        :param centre: array-like container of floats, location of cell centre
        :param active: bool, if cell is currently active
        :param size: float, size of cell
        :param dimension: int, dimension of cell, calculated from centre
        """
        self.centre = centre
        self.size = size
        self.active = active
        if len(centre) != dimension :
            self.dimension = len(centre)

    def __str__(self):
        rep = "-"*5+"SimpleCellRes cell"+"-"*5
        rep += "\n+++ centre = {}".format(self.centre)
        rep += "\n+++ size = {:<6}".format(self.size)
        rep += "\n+++ dimension = {}".format(self.dimension)
        is_active = lambda x: "ACTIVE" if x is True else "INACTIVE"
        rep += "\n+++ {}".format(is_active(self.active))
        rep += "\n"+"-"*28
        return rep
