[![Build Status](https://travis-ci.org/tcollier/spiral.svg?branch=master)](https://travis-ci.org/tcollier/spiral)

# Spiral Matrix Traversal

Iterate over a 2-D matrix in a spiral path, e.g.

## Usage

### Installation

```bash
pipenv install tcollier-spiral
```

### Example

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

# Misc

[See research documentation](docs/research.md)
