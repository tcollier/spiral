[![Build Status](https://travis-ci.org/tcollier/spiral.svg?branch=master)](https://travis-ci.org/tcollier/spiral)

# Spiral Matrix Traversal

Iterate over a 2-D matrix in a clockwise or counter-clockwise spiral path.

## Usage

### Installation

```bash
pipenv install tcollier-spiral
```

### Clockwise Example

```python
from spiral.spiral_matrix import SpiralMatrix

matrix = SpiralMatrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]])

for item in matrix:
    print(item)
# 1
# 2
# 3
# 4
# 8
# 12
# 11
# 10
# 9
# 5
# 6
# 7
```

### Counter-clockwise Example

```python
from spiral.spiral_matrix import SpiralMatrix

ccw_matrix = SpiralMatrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]],
    clockwise=False)

# Alternatively:
#
# cw_matrix = SpiralMatrix([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]])
# ccw_matrix = reversed(cw_matrix)

for item in ccw_matrix:
    print(item)
# 1
# 5
# 9
# 10
# 11
# 12
# 8
# 4
# 3
# 2
# 6
# 7
```

# Misc

[See research documentation](docs/research.md)
