[![Build Status](https://travis-ci.org/tcollier/spiral.svg?branch=master)](https://travis-ci.org/tcollier/spiral)

# Spiral Matrix Traversal

I've implemented several different algorithms to traverse a matrix in a
clockwise or counter-clockwise path.

## Algorithms

Each algorithm is implemented as a visitor class, that applies a visit function
to each element as it is visited.

### Dequeue Visitor

Visit each element of a matrix in a spiral path using a deque of deques. The
initial deque is a duplicate of the matrix, but is destructively consumed as it
it traversed.

[code](../spiral/research/visitor/deque_visitor.py)

### Iterative Visitor

Visit each element of a matrix in a spiral path using an iterative approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.

[code](../spiral/research/visitor/iterative_visitor.py)

### Margin Visitor

Visit each element of a matrix in a spiral path by keeping track of an
increasing "margin". Each time we traverse one rotation in the spiral, the
margin on all sides increases by one.

[code](../spiral/research/visitor/margin_visitor.py)

### Recursive Visitor

Visit each element of a matrix in a spiral path using a recursive approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.

This algorithm is unable to traverse large matrices as the recursion stack will
overflow and raise a `RecursionError`

[code](../spiral/research/visitor/recursive_visitor.py)

# Performance Benchmarking

For a 20x20 matrix, pytest-benchmark points to DequeVisitor as the most performant
by a large margin

```
--------------------------------------------------------------------------------------------------- benchmark: 4 tests --------------------------------------------------------------------------------------------------
Name (time in us)                              Min                   Max                  Mean              StdDev                Median                IQR            Outliers         OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_deque_visitor_large_matrix           147.2720 (1.0)      1,569.3510 (1.0)        187.9653 (1.0)       23.7879 (1.0)        185.8370 (1.0)       5.2193 (1.0)       278;448  5,320.1308 (1.0)        4349           1
test_margin_visitor_large_matrix        1,074.5450 (7.30)     1,638.1170 (1.04)     1,514.0232 (8.05)      46.1966 (1.94)     1,516.6010 (8.16)     45.0700 (8.64)        80;15    660.4918 (0.12)        620           1
test_iterative_visitor_large_matrix     2,527.3120 (17.16)    3,842.2200 (2.45)     3,332.0948 (17.73)    147.3448 (6.19)     3,356.2965 (18.06)    62.6740 (12.01)       19;19    300.1115 (0.06)        290           1
test_recursive_visitor_large_matrix     3,079.3190 (20.91)    3,857.7890 (2.46)     3,646.8191 (19.40)    174.2009 (7.32)     3,703.7530 (19.93)    73.5348 (14.09)       29;35    274.2116 (0.05)        217           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
