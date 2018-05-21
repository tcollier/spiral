"""
Track which elements in a matrix can be visited
"""


class VisitTracker(object):
    def __init__(self, matrix):
        self.__visited = [[False for _ in vector] for vector in matrix]

    def visit(self, i, j):
        """
        :param location: The location within the array that has been visited
        """
        self.__visited[i][j] = True

    def visitable(self, i, j):
        """
        :param location: The location within the matrix to check whether it can
        be visited
        :return: True if the location is in bounds for the matrix (i.e. `i` and
        `j` are not less than zero or greater/equal to the length of the matrix
        vectors) and has not already been visited, otherwise False
        """
        i_in_bounds = 0 <= i < len(self.__visited)
        if not i_in_bounds:
            return False

        j_in_bounds = 0 <= j < len(self.__visited[0])
        if not j_in_bounds:
            return False

        return not self.__visited[i][j]
