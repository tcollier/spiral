"""
Simple encapsulation for a location within a matrix. Changes in `i` represent
movement up (smaller values) and down (larger values) within a column vector.
Changes in `j` represent movement left (smaller values) and right (larger
values) within a row vector.
"""
from collections import namedtuple


Location = namedtuple('Location', 'i j')
