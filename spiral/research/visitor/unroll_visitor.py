class UnrollVisitor(object):
    def __init__(self, visit_fn):
        self.__visit_fn = visit_fn

    def start(self, matrix, clockwise):
        traverse_fn = (self.__cw if clockwise else self.__ccw)
        traverse_fn(matrix)

    def __cw(self, matrix):
        [self.__visit_fn(i) for i in matrix[0]]
        if len(matrix) > 1:
            self.__cw([list(v) for v in list(zip(*matrix[1:]))[::-1]])

    def __ccw(self, matrix):
        [self.__visit_fn(i[0]) for i in matrix]
        if len(matrix[0]) > 1:
            self.__ccw([list(v) for v in list(zip(*matrix[::-1]))[1:]])
