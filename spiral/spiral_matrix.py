from spiral.inward_clockwise_spiral_matrix import InwardClockwiseSpiralMatrix
from spiral.inward_counter_clockwise_spiral_matrix import (
    InwardCounterClockwiseSpiralMatrix)
from spiral.outward_clockwise_spiral_matrix import OutwardClockwiseSpiralMatrix
from spiral.outward_counter_clockwise_spiral_matrix import (
    OutwardCounterClockwiseSpiralMatrix)


class SpiralMatrix(object):
    def __init__(self, matrix, clockwise=True, inward=True):
        self.__matrix = matrix
        self.__clockwise = clockwise
        self.__inward = inward

    def __reversed__(self):
        return SpiralMatrix(
            self.__matrix, clockwise=not self.__clockwise,
            inward=not self.__inward)

    def __iter__(self):
        if not self.__matrix or not self.__matrix[0]:
            return

        if self.__inward:
            if self.__clockwise:
                delegate_class = InwardClockwiseSpiralMatrix
            else:
                delegate_class = InwardCounterClockwiseSpiralMatrix
        else:
            if self.__clockwise:
                delegate_class = OutwardClockwiseSpiralMatrix
            else:
                delegate_class = OutwardCounterClockwiseSpiralMatrix

        delegate = delegate_class(matrix=self.__matrix)
        for i in delegate:
            yield i
