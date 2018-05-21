"""
Enumerate lambdas for moving a location by one item for each of the four
possible directions.
"""
from enum import Enum


class Direction(Enum):
    RIGHT = lambda i, j: (i, j + 1)
    DOWN = lambda i, j: (i + 1, j)
    LEFT = lambda i, j: (i, j - 1)
    UP = lambda i, j: (i - 1, j)
