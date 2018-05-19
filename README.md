[![Build Status](https://travis-ci.org/tcollier/spiral.svg?branch=master)](https://travis-ci.org/tcollier/spiral)

# Spiral Matrix Traversal

Several different implementations of algorithms to traverse a matrix in a
clockwise or counter-clockwise path

## Algorithms

Each algorithm is implemented as a visitor class, that applies a visit function
to each element as it is visited.

### Dequeue Visitor

Visit each element of a matrix in a spiral path using a deque of deques. The
initial deque is a duplicate of the matrix, but is destructively consumed as it
it traversed.

### Iterative Visitor

Visit each element of a matrix in a spiral path using an iterative approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.

### Margin Visitor

Visit each element of a matrix in a spiral path by keeping track of an
increasing "margin". Each time we traverse one rotation in the spiral, the
margin on all sides increases by one.

### Recursive Visitor

Visit each element of a matrix in a spiral path using a recursive approach.
This algorithm keeps track of which elements have already been visited to ensure
that no element is visited twice.
