"""
Traverse a matrix in a clockwise or counter clockwise spiral, applying a visit
function to each element when it is visited.
"""


class Traverser(object):
    def __init__(self, matrix):
        self.__matrix = matrix

    def start(self, visitor, clockwise=True):
        """
        :param visitor: Visitor class that visits each element in the matrix in
        a spiral path
        :param clockwise: If True, then visit each element in a clockwise
        spiral, otherwise visit in a counter-clockwise spiral
        """
        if not len(self.__matrix) or not len(self.__matrix[0]):
            return

        visitor.start(self.__matrix, clockwise)
