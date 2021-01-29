"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because
of the exotic matter involved. It starts as raw ore, then during
processing, begins randomly changing between forms, eventually reaching
a stable form. There may be multiple stable forms that a sample could
ultimately reach, not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase
fuel creation efficiency by predicting the end state of a given ore
sample. You have carefully studied the different structures that the
ore can take and which transitions it undergoes. It appears that, while
random, the probability of each structure transforming is fixed. That
is, each time the ore is in 1 state, it has the same probabilities of
entering the next state (which might be the same state).  You have
recorded the observed transitions in a matrix. The others in the lab
have hypothesized more exotic forms that the ore can become, but you
haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative
ints representing how many times that state has gone to the next state
and return an array of ints for each terminal state giving the exact
probabilities of each terminal state, represented as the numerator for
each state, then the denominator for all of them at the end and in
simplest form. The matrix is at most 10 by 10. It is guaranteed that no
matter which state the ore is in, there is a path from that state to a
terminal state. That is, the processing will always eventually end in a
stable state. The ore starts in state 0. The denominator will fit within
a signed 32-bit integer during the calculation, as long as the fraction
is simplified regularly.

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input
Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
Output:
    [7, 6, 8, 21]

Input:
Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    [0, 3, 2, 9, 14]

-- Python cases --
Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]
"""
from fractions import Fraction
from fractions import gcd


def fraction(numerator, denominator=1):
    return 0 if numerator == 0 else Fraction(numerator, denominator)


def subtract(a, b):
    # subtract matrix b from a
    n = xrange(len(a))
    return [[a[i][j] - b[i][j] for j in n] for i in n]


def identity(m):
    # identity matrix for matrix m
    n = xrange(len(m))
    return [[1 if i == j else 0 for j in n] for i in n]


def multiply(a, b):
    # multiply matrices a x b
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]


def invert(a):
    # https://github.com/ThomIves/MatrixInverse/blob/master/MatrixInversion.py
    b = identity(a)
    for d in xrange(len(a)):
        to1 = fraction(1, a[d][d])
        for j in xrange(len(a)):
            a[d][j] *= to1
            b[d][j] *= to1
        for i in range(len(a))[0:d] + range(len(a))[d + 1 :]:
            to0 = a[i][d]
            for j in xrange(len(a)):
                a[i][j] = a[i][j] - to0 * a[d][j]
                b[i][j] = b[i][j] - to0 * b[d][j]
    return b


def lcm(a):
    # least common multiple for array
    for i, x in enumerate(a):
        lcm = x if i == 0 else lcm * x // gcd(lcm, x)
    return lcm


def solution(m):
    """
    This problem describes an absorbing Markov Chain.
    https://en.wikipedia.org/wiki/Absorbing_Markov_chain

    The provided data is almost in canonical form, P.  With this matrix,
    we can then use its properties to determine B, the probabilities of
    ending up in a particular absorbing (terminal) state.
              _       _
             |         |
             |  Q   R  |
        P =  |         |
             |  0   I  |
             |_       _|

                        -1
        B =  ( I  -  Q )   * R
    """

    terminal = [not any(row) for row in m]

    if terminal.count(True) == 1:
        return [1, 1]

    p = [
        [
            1
            if terminal[state] and state == next_state
            else fraction(prob, sum(m[state]))
            for next_state, prob in enumerate(probs)
        ]
        for state, probs in enumerate(m)
    ]

    q = [
        [p[i][j] for j, is_terminal in enumerate(terminal) if not is_terminal]
        for i, is_terminal in enumerate(terminal)
        if not is_terminal
    ]

    r = [
        [p[i][j] for j, is_terminal in enumerate(terminal) if is_terminal]
        for i, is_terminal in enumerate(terminal)
        if not is_terminal
    ]

    # probabilities for starting in state 0
    b0 = multiply(invert(subtract(identity(q), q)), r)[0]

    common = lcm([x.denominator for x in b0])

    return [x.numerator * common / x.denominator for x in b0] + [common]
