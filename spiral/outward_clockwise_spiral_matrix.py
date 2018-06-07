from spiral.outward_spiral_matrix import OutwardSpiralMatrix


class OutwardClockwiseSpiralMatrix(OutwardSpiralMatrix):
    def __iter__(self):
        if self.is_wide:
            margin_change = self.UP

            if self.has_even_height:
                #
                #  X ┌-------┐
                #  ┆ ┆ ▷---┐ ┆
                #  ┆ └-----┘ ┆
                #  └---------┘
                #
                i = self.height // 2 - 1
                margin = i
                j = i + 1
                direction_index = self.RIGHT
            else:
                #
                #  X ┌-------┐
                #  ┆ └-----◁ ┆
                #  └---------┘
                #
                i = self.height // 2
                margin = i
                j = self.width - i - 1
                direction_index = self.LEFT
        else:
            j = self.width // 2
            margin_change = self.LEFT

            if self.has_even_width:
                #
                #  X ┌---┐
                #  ┆ ┆ ▽ ┆
                #  ┆ ┆ ┆ ┆
                #  ┆ ┆ ┆ ┆
                #  ┆ └-┘ ┆
                #  └-----┘
                #
                i = j - 1
                margin = i
                direction_index = self.DOWN
            else:
                #
                #  X ┌-┐
                #  ┆ ┆ ┆
                #  ┆ ┆ ┆
                #  ┆ ┆ ┆
                #  ┆ △ ┆
                #  └---┘
                #
                i = self.height - j - 1
                margin = j - 1
                direction_index = self.UP

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
                direction_index = direction_index + 1
                direction_index %= 4
                direction = self.COMPASS[direction_index]

                i, j = i + direction[0], j + direction[1]
