"""
Enumerate lambdas for moving a location by one item for each of the four
possible directions.
"""
from enum import Enum
from .location import Location


class Direction(Enum):
    RIGHT = lambda location: Location(location.i, location.j + 1)
    DOWN = lambda location: Location(location.i + 1, location.j)
    LEFT = lambda location: Location(location.i, location.j - 1)
    UP = lambda location: Location(location.i - 1, location.j)
