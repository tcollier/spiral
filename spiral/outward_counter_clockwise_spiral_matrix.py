from spiral.outward_spiral_matrix import OutwardSpiralMatrix


class OutwardCounterClockwiseSpiralMatrix(OutwardSpiralMatrix):
    def __iter__(self):
        if self.is_tall:
            margin_change = self.UP

            if self.has_even_width:
                #
                #  X-----┐
                #  ┌---┐ ┆
                #  ┆ ▽ ┆ ┆
                #  ┆ ┆ ┆ ┆
                #  ┆ └-┘ ┆
                #  └-----┘
                #
                j = self.width // 2 - 1
                i = j + 1
                margin = j
                direction_index = self.DOWN
            else:
                #
                #  X---┐
                #  ┌-┐ ┆
                #  ┆ ┆ ┆
                #  ┆ ┆ ┆
                #  ┆ △ ┆
                #  └---┘
                #
                j = self.width // 2
                i = self.height - j - 1
                margin = j
                direction_index = self.UP
        else:
            i = self.height // 2
            margin = i - 1
            margin_change = self.UP

            if self.has_even_height:
                #
                #  X---------┐
                #  ┌-------┐ ┆
                #  ┆ ▷-----┘ ┆
                #  └---------┘
                #
                j = i - 1
                direction_index = 0
            else:
                #
                #  X---------┐
                #  ┌-------◁ ┆
                #  └---------┘
                #
                j = self.width - i - 1
                direction_index = self.LEFT

        for _ in range(self.num_elements):
            yield self._matrix[i][j]

            direction = self.COMPASS[direction_index]
            i2 = i + direction[0]
            j2 = j + direction[1]
            if margin <= i2 < self.height - margin and margin <= j2 < self.width - margin:
                i, j = i2, j2
            else:
                if direction_index == margin_change:
                    margin -= 1

                # Turn 90 degrees in the proper direction
                direction_index = direction_index - 1
                direction_index %= 4
                direction = self.COMPASS[direction_index]

                i, j = i + direction[0], j + direction[1]
