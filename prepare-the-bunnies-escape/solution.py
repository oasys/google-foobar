"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and
freeing Commander Lambda's bunny workers, but once they're free of the
work duties the bunnies are going to need to escape Lambda's space
station via the escape pods as quickly as possible. Unfortunately,
the halls of the space station are a maze of corridors and dead ends
that will be a deathtrap for the escaping bunnies. Fortunately,
Commander Lambda has put you in charge of a remodeling project that
will give you the opportunity to make things a little easier for the
bunnies. Unfortunately (again), you can't just remove all obstacles
between the bunnies and the escape pods - at most you can remove one
wall per escape pod path, both to maintain structural integrity of the
station and to avoid arousing Commander Lambda's suspicions.

You have maps of parts of the space station, each starting at a
work area exit and ending at the door to an escape pod. The map is
represented as a matrix of 0s and 1s, where 0s are passable space and
1s are impassable walls. The door out of the station is at the top left
(0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

Write a function solution(map) that generates the length of the shortest
path from the station door to the escape pod, where you are allowed to
remove one wall as part of your remodeling plans. The path length is
the total number of nodes you pass through, counting both the entrance
and exit nodes. The starting and ending positions are always passable
(0). The map will always be solvable, though you may or may not need
to remove a wall. The height and width of the map can be from 2 to
20. Moves can only be made in cardinal directions; no diagonal moves are
allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11

-- Java cases --
Input:
Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
Output:
    7

Input:
Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
Output:
    11
"""


def distance(map):
    # count up distance to each node from start location
    notseen = 999
    d = [
        [1 if i == j == 0 else notseen for j in xrange(len(row))]
        for i, row in enumerate(map)
    ]

    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x2, y2 = x + move[0], y + move[1]
            if 0 <= x2 < len(d) and 0 <= y2 < len(d[0]):
                if d[x2][y2] == notseen:
                    d[x2][y2] = d[x][y] + 1
                    if not map[x2][y2]:
                        q.append((x2, y2))
    return d


def flip(map):
    # flip a map to have the "end" at (0,0)
    return [[v for v in reversed(row)] for row in reversed(map)]


def solution(map):
    # find the distances starting from both entrance and exit
    b = distance(map)
    e = flip(distance(flip(map)))
    # add the distances and find the shortest point where they intersect
    return min([sum(v) - 1 for i, _ in enumerate(map) for v in zip(b[i], e[i])])
