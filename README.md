
# [Google Foobar Challenge](https://github.com/oasys/google-foobar)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

&copy; 2021 Jason Lavoie

## What is the Google Foobar Challenge

[Google Foobar challenge][foobar] is a set of programming challenges.
It is reported that Google has used this as recruiting tool to find
candidate developers to hire.  (Indeed, there's a `recruitme` command
available once you reach the upper levels.)  It consists of a (somewhat
contrived) sci-fi adventure story where you are the hero trying to
stop an evil antagonist from destroying a planet solving programming
challenges of increasing difficulty to advance the plot.

[foobar]: https://foobar.withgoogle.com

## Disclaimer

I am sharing this code both to document my work and for others who may
not (yet) have access to the challenges.  If you _are_ currently taking
the Foobar Challenge, please do not copy these solutions.  Doing so will
deprive you of the fun and learning of working through the problems
yourself.

## Notes

- Since many of the problem statements included explicit instructions
about the parameters of the problem, I expected that the verification
tests would include invalid or out-of-bounds input data.  I quickly
realized that the verification tests are only checking corner cases
to make sure that you implement the algorithm correctly.  In the
interests of focusing on the solution, I omitted any bounds checking or
assertions that weren't absolutely required.

- My solutions strive for elegance and brevity, in order to focus on the
algorithm itself.

- Each challenge is authored to target a single algorithm or technique.
Some were already known to me, others required a bit of learning.  I
used this as my guide: if my proposed approach was too complicated, look
for something simpler.

## The Challenges

The challenges were grouped into five levels, 1 through 5.  You must
complete a challenge to request the next.  As some levels have more than
one challenge, you must complete all those in a level to advance to the
next level.

The interface provides test cases for each challenge.  The inputs and
expected outputs for the first few tests are documented, but each
challenge also contains additional "hidden" tests.  The test suite
can be run at any time with the `verify` command.  Once all tests are
passing, the `submit` command will check the provided solution and
proceed to the next challenge.

The challenges can be solved in either Java or Python.  There are
documented constraints, such as no I/O and limited version/libraries:

> Your code will run inside a Python 2.7.6 sandbox. Standard libraries
> are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat,
> select, signal, termios, thread, time, unicodedata, zipimport, zlib.

There is a time limit for each question, but in my experience these were
very generous.  For example, the final challenge allocated "528 hours"
to complete.  It took me just under a week working in my spare time to
complete all the challenges.

### Level 1

#### Challenge 1.1 "Solar Doomsday"

This first challenge really whet my appetite, as it allowed me to write
a recursive function to divide up an area into its largest squares.

<details><summary>description</summary>

> Who would've guessed? Doomsday devices take a LOT of power. Commander
> Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor
> core with solar arrays, and she's tasked you with setting up the solar
> panels.
>
> Due to the nature of the space station's outer paneling, all of its
> solar panels must be squares. Fortunately, you have one very large and
> flat area of solar material, a pair of industrial-strength scissors,
> and enough MegaCorp Solar Tape(TM) to piece together any excess panel
> material into more squares. For example, if you had a total area of 12
> square yards of solar material, you would be able to make one 3x3 square
> panel (with a total area of 9). That would leave 3 square yards, so you
> can turn those into three 1x1 square solar panels.
>
> Write a function solution(area) that takes as its input a single unit of
> measure representing the total area of solar panels you have (between 1
> and 1000000 inclusive) and returns a list of the areas of the largest
> squares you could make out of those panels, starting with the largest
> squares first. So, following the example above, solution(12) would
> return [9, 1, 1, 1].

</details>

<details open><summary>solution</summary>

```python

from math import sqrt


def solution(area):
    # return list of the areas of the largest squares
    # that can be made out of the provided area, largest first
    if area < 1 or area > 1000000:
        raise ValueError("area should be between 1 and 1000000 inclusive")
    if sqrt(area).is_integer():
        return [area]
    biggest = int(sqrt(area)) ** 2
    return [biggest] + solution(area - biggest)

```

</details>

### Level 2

#### Challenge 2.1 "Numbers Station Coded Messages"

The second challenge was solved with a function that incrementally walked
through an array, returning the starting indexes within the array where
the elements add up to the given total.

<details><summary>description</summary>

> When you went undercover in Commander Lambda's organization, you set
> up a coded messaging system with Bunny Headquarters to allow them to
> send you important mission updates. Now that you're here and promoted
> to Henchman, you need to make sure you can receive those messages - but
> since you need to sneak them past Commander Lambda's spies, it won't be
> easy!
>
> Bunny HQ has secretly taken control of two of the galaxy's more
> obscure numbers stations, and will use them to broadcast lists of
> numbers. They've given you a numerical key, and their messages will be
> encrypted within the first sequence of numbers that adds up to that key
> within any given list of numbers.
>
> Given a non-empty list of positive integers l and a target positive
> integer t, write a function solution(l, t) which verifies if there is at
> least one consecutive sequence of positive integers within the list l
> (i.e. a contiguous sub-list) that can be summed up to the given target
> positive integer t (the key) and returns the lexicographically smallest
> list containing the smallest start and end indexes where this sequence
> can be found, or returns the array [-1, -1] in the case that there is no
> such sequence (to throw off Lambda's spies, not all number broadcasts
> will contain a coded message).
>
> For example, given the broadcast list l as [4, 3, 5, 7, 8] and the
> key t as 12, the function solution(l, t) would return the list [0, 2]
> because the list l contains the sub-list [4, 3, 5] starting at index 0
> and ending at index 2, for which 4 + 3 + 5 = 12, even though there is a
> shorter sequence that happens later in the list (5 + 7). On the other
> hand, given the list l as [1, 2, 3, 4] and the key t as 15, the function
> solution(l, t) would return [-1, -1] because there is no sub-list of
> list l that can be summed up to the given target value t = 15.
>
> To help you identify the coded broadcasts, Bunny HQ has agreed to the
> following standards:
>
> - Each list l will contain at least 1 element but never more than 100.
> - Each element of l will be between 1 and 100.
> - t will be a positive integer, not exceeding 250.
> - The first element of the list l has index 0.
> - For the list returned by solution(l, t), the start index must be
>   equal or smaller than the end index.
>
> Remember, to throw off Lambda's spies, Bunny HQ might include more than
> one contiguous sublist of a number broadcast that can be summed up to
> the key. You know that the message will always be hidden in the first
> sublist that sums up to the key, so solution(l, t) should only return
> that sublist.

</details>

<details open><summary>solution</summary>

```python

def solution(l, t):
    # return first beginning and end indexes in l whose values add up to t
    for start in range(len(l)):
        total = 0
        for current, e in enumerate(l[start:]):
            total += e
            if total == t:
                return [start, start + current]
            if total > t:
                break
    return [-1, -1]

```

</details>

#### Challenge 2.2 "Elevator Maintenance"

The third challenge boils down to sorting [Semantic
Versioning](https://semver.org) version numbers.

<details><summary>description</summary>

> You've been assigned the onerous task of elevator maintenance - ugh! It
> wouldn't be so bad, except that all the elevator documentation has been
> lying in a disorganized pile at the bottom of a filing cabinet for
> years, and you don't even know what elevator version numbers you'll be
> working on.
>
> Elevator versions are represented by a series of numbers, divided up
> into major, minor and revision integers. New versions of an elevator
> increase the major number, e.g. 1, 2, 3, and so on. When new features
> are added to an elevator without being a complete new version, a second
> number named "minor" can be used to represent those new additions,
> e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be
> represented by a third number named "revision", e.g. 1.1.1, 1.1.2,
> 1.2.0, and so on. The number zero can be used as a major for pre-release
> versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is
> careful to always beta test her new technology, with her loyal henchmen
> as subjects!).
>
> Given a list of elevator versions represented as strings, write a
> function solution(l) that returns the same list sorted in ascending
> order by major, minor, and revision number so that you can identify the
> current elevator version. The versions in list l will always contain
> major numbers, but minor and revision numbers are optional. If the
> version contains a revision number, then it will also have a minor
> number.
>
> For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12",
> "1.0.2"], the function solution(l) would return the list ["1.0",
> "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are
> equivalent but one version contains more numbers than the others, then
> these versions must be sorted ascending based on how many numbers they
> have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l
> will be at least 1 and will not exceed 100.

</details>

<details open><summary>solution</summary>

```python

def solution(l):
    # sorts semver versions by major/minor/integer
    l.sort(key=lambda val: [int(section) for section in val.split(".")])
    return l
```

</details>

### Level 3

#### Challenge 3.1 "Fuel Injection Perfection"

At this point, I thought I could quickly blast through the challenges
but this one gave me pause.  Given a number, return the count of the
fewest operations (add, subtract, or halve) to reduce the number to 1.

The first part was simple, if the number is even, halve it, otherwise
subtract one.  But in some cases, like for the number 7, it is best
to add one first.  Intuitively, I knew that this had to do with powers
of two, so I considered the binary representation until I saw a
pattern.

<details><summary>description</summary>

> Commander Lambda has asked for your help to refine the automatic quantum
> antimatter fuel injection system for her LAMBCHOP doomsday device. It's
> a great chance for you to get a closer look at the LAMBCHOP - and maybe
> sneak in a bit of sabotage while you're at it - so you took the job
> gladly.
>
> Quantum antimatter fuel comes in small pellets, which is convenient
> since the many moving parts of the LAMBCHOP each need to be fed fuel one
> pellet at a time. However, minions dump pellets in bulk into the fuel
> intake. You need to figure out the most efficient way to sort and shift
> the pellets down to a single pellet at a time.
>
> The fuel control mechanisms have three operations:
>
> 1) Add one fuel pellet
> 2) Remove one fuel pellet
> 3) Divide the entire group of fuel pellets by 2 (due to the destructive
>    energy released when a quantum antimatter pellet is cut in half, the
>    safety controls will only allow this to happen if there is an even
>    number of pellets)
>
> Write a function called solution(n) which takes a positive integer as a
> string and returns the minimum number of operations needed to transform
> the number of pellets to 1. The fuel intake control panel can only
> display a number up to 309 digits long, so there won't ever be more
> pellets than you can express in that many digits.
>
> For example:
>
> - solution(4) returns 2: 4 -> 2 -> 1
> - solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

</details>

<details open>
  <summary>solution</summary>

```python

def solution(n):
    # count min number of add/subtract/halve operations to reach 1
    n = int(n)
    count = 0
    while n != 1:
        if n % 2:  # odd
            if n % 4 == 1 or n == 3:
                n -= 1  # subtract is better
            else:
                n += 1  # otherwise add
        else:  # even, halve
            n /= 2
        count += 1
    return count
```

</details>

#### Challenge 3.2 "Doomsday Fuel"

This challenge is where I *really* got hooked.  It was obvious from
the description that the writer was targeting a specific algorithm or
methodology, but I had no idea initially what that was.  My first search
for "terminal states probability" turned up the jackpot, a [Wikipedia
Article](https://en.wikipedia.org/wiki/Absorbing_Markov_chain) on
absorbing Markov chains.  This seemed to describe the problem exactly.
I only had to convert the provided matrix to canonical form, and use
the formula to find the probabilities.

Despite solving this rather quickly, I spent the weekend going
down a rabbit hole learning about Markov chains and their other
applications.  Since it is not permitted to use modules like
[numpy](https://numpy.org), I also had to write my own matrix
functions.  Thom Ives' [post][ives] on the [Integrated ML and AI
site](https://integratedmlai.com) proved very helpful, especially with
matrix inversion.

[ives]: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/

<details><summary>description</summary>

> Making fuel for the LAMBCHOP's reactor core is a tricky process because
> of the exotic matter involved. It starts as raw ore, then during
> processing, begins randomly changing between forms, eventually reaching
> a stable form. There may be multiple stable forms that a sample could
> ultimately reach, not all of which are useful as fuel.
>
> Commander Lambda has tasked you to help the scientists increase
> fuel creation efficiency by predicting the end state of a given ore
> sample. You have carefully studied the different structures that the
> ore can take and which transitions it undergoes. It appears that, while
> random, the probability of each structure transforming is fixed. That
> is, each time the ore is in 1 state, it has the same probabilities of
> entering the next state (which might be the same state).  You have
> recorded the observed transitions in a matrix. The others in the lab
> have hypothesized more exotic forms that the ore can become, but you
> haven't seen all of them.
>
> Write a function solution(m) that takes an array of array of nonnegative
> ints representing how many times that state has gone to the next state
> and return an array of ints for each terminal state giving the exact
> probabilities of each terminal state, represented as the numerator for
> each state, then the denominator for all of them at the end and in
> simplest form. The matrix is at most 10 by 10. It is guaranteed that no
> matter which state the ore is in, there is a path from that state to a
> terminal state. That is, the processing will always eventually end in a
> stable state. The ore starts in state 0. The denominator will fit within
> a signed 32-bit integer during the calculation, as long as the fraction
> is simplified regularly.
>
> For example, consider the matrix m:
>
> ```python
> [
>   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
>   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
>   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
>   [0,0,0,0,0,0],  # s3 is terminal
>   [0,0,0,0,0,0],  # s4 is terminal
>   [0,0,0,0,0,0],  # s5 is terminal
> ]
> ```
>
> So, we can consider different paths to terminal states, such as:
>
> - s0 -> s1 -> s3
> - s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
> - s0 -> s1 -> s0 -> s5
>
> Tracing the probabilities of each, we find that
>
> - s2 has probability 0
> - s3 has probability 3/14
> - s4 has probability 1/7
> - s5 has probability 9/14
>
> So, putting that together, and making a common denominator, gives an
> answer in the form of
>
> [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
> [0, 3, 2, 9, 14].

</details>

<details open>
  <summary>solution</summary>

```python

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

```

</details>

#### Challenge 3.3 "Prepare the Bunnies Escape"

This challenge asked to find the location of the one
wall in a maze that, if removed, would provide the
shortest path between `[0,0]` and the opposite corner.  My
networking bias made me first think of [Dijkstra's SPF
algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm),
but upon consideration it seemed too complex to recalculate
SPF for each wall section.  I ended up doing a [breadth-first
search](https://en.wikipedia.org/wiki/Breadth-first_search) starting
from each corner, counting up the distance.  I also counted (one step)
into each wall I encountered.  By pairwise summing these two sets of
distances, the lowest number is the wall that would need to be removed.

<details><summary>description</summary>

> You're awfully close to destroying the LAMBCHOP doomsday device and
> freeing Commander Lambda's bunny workers, but once they're free of the
> work duties the bunnies are going to need to escape Lambda's space
> station via the escape pods as quickly as possible. Unfortunately,
> the halls of the space station are a maze of corridors and dead ends
> that will be a deathtrap for the escaping bunnies. Fortunately,
> Commander Lambda has put you in charge of a remodeling project that
> will give you the opportunity to make things a little easier for the
> bunnies. Unfortunately (again), you can't just remove all obstacles
> between the bunnies and the escape pods - at most you can remove one
> wall per escape pod path, both to maintain structural integrity of the
> station and to avoid arousing Commander Lambda's suspicions.
>
> You have maps of parts of the space station, each starting at a
> work area exit and ending at the door to an escape pod. The map is
> represented as a matrix of 0s and 1s, where 0s are passable space and
> 1s are impassable walls. The door out of the station is at the top left
> (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).
>
> Write a function solution(map) that generates the length of the shortest
> path from the station door to the escape pod, where you are allowed to
> remove one wall as part of your remodeling plans. The path length is
> the total number of nodes you pass through, counting both the entrance
> and exit nodes. The starting and ending positions are always passable
> (0). The map will always be solvable, though you may or may not need
> to remove a wall. The height and width of the map can be from 2 to
> 20. Moves can only be made in cardinal directions; no diagonal moves are
> allowed.

</details>

<details open><summary>solution</summary>

```python

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

```

</details>

### Level 4

#### Challenge 4.1 "Free The Bunny Workers"

<details><summary>description</summary>

> You need to free the bunny workers before Commander Lambda's space
> station explodes! Unfortunately, the Commander was very careful with the
> highest-value workers -- they all work in separate, maximum-security
> work rooms. The rooms are opened by putting keys into each console, then
> pressing the open button on each console simultaneously. When the open
> button is pressed, each key opens its corresponding lock on the work
> room. So, the union of the keys in all of the consoles must be all of
> the keys. The scheme may require multiple copies of one key given to
> different minions.
>
> The consoles are far enough apart that a separate minion is needed for
> each one. Fortunately, you have already relieved some bunnies to aid
> you - and even better, you were able to steal the keys while you were
> working as Commander Lambda's assistant. The problem is, you don't know
> which keys to use at which consoles. The consoles are programmed to know
> which keys each minion had, to prevent someone from just stealing all of
> the keys and using them blindly. There are signs by the consoles saying
> how many minions had some keys for the set of consoles. You suspect that
> Commander Lambda has a systematic way to decide which keys to give to
> each minion such that they could use the consoles.
>
> You need to figure out the scheme that Commander Lambda used to
> distribute the keys. You know how many minions had keys, and how many
> consoles are by each work room.  You know that Command Lambda wouldn't
> issue more keys than necessary (beyond what the key distribution scheme
> requires), and that you need as many bunnies with keys as there are
> consoles to open the work room.
>
> Given the number of bunnies available and the number of locks required
> to open a work room, write a function solution(num_buns, num_required)
> which returns a specification of how to distribute the keys such
> that any num_required bunnies can open the locks, but no group of
> (num_required - 1) bunnies can.
>
> Each lock is numbered starting from 0. The keys are numbered the same
> as the lock they open (so for a duplicate key, the number will repeat,
> since it opens the same lock). For a given bunny, the keys they get
> is represented as a sorted list of the numbers for the keys. To cover
> all of the bunnies, the final solution is represented by a sorted list
> of each individual bunny's list of keys.  Find the lexicographically
> least such key distribution - that is, the first bunny should have keys
> sequentially starting from 0.
>
> num_buns will always be between 1 and 9, and num_required will always be
> between 0 and 9 (both inclusive).  For example, if you had 3 bunnies and
> required only 1 of them to open the cell, you would give each bunny the
> same key such that any of the 3 of them would be able to open it, like
> so:
>
> ```python
> [
>   [0],
>   [0],
>   [0],
> ]
> ```
>
> If you had 2 bunnies and required both of them to open the cell, they
> would receive different keys (otherwise they wouldn't both actually be
> required), and your solution would be as follows:
>
> ```python
> [
>   [0],
>   [1],
> ]
> ```
>
> Finally, if you had 3 bunnies and required 2 of them to open the cell,
> then any 2 of the 3 bunnies should have all of the keys necessary to
> open the cell, but no single bunny would be able to do it.  Thus, the
> solution would be:
>
> ```python
> [
>   [0, 1],
>   [0, 2],
>   [1, 2],
> ]
>
> ```

</details>

<details open><summary>solution</summary>

```python

def solution(num_buns, num_required):
    c = list(combinations(range(num_buns), num_buns - (num_required - 1)))
    return [
        [key for key, bunnies in enumerate(c) if bunny in bunnies]
        for bunny in xrange(num_buns)
    ]

```

</details>

#### Challenge 4.2 "Bringing a Gun to a Trainer Fight"

This was my favorite challenge, and the one where I'm most proud
of the solution.  It was also the one which I spent the most time
thinking about.  Given the location of two people in a room of specified
dimensions with perfect reflection, find the total number of angles that
beam weapon could be fired to hit the other person without hitting you
first or reaching its maximum range.

My first thought was to rotate the room around the target.  I fantasized
about reviving graphics algorithms from old assembly demos, but nothing
seemed to pan out.  I worked for a bit of modeling the room as a matrix
and translating it to a larger field with reflections, but the code
proved too complicated, so I went to bed.

Inspiration struck while walking the dog the next morning.
I came up with a solutino where I projected points of all
the possible reflected targets (either person) out into 2D
space, and calculated the distance (by use of the [Pythagorean
theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem)) and the
bearing (using `atan2()`) back to the hero's original coordinates.
Ignoring any "hits" that intersected a closer target left only the ones
that we needed to count.

By originating the "room" at `[0, 0]` in the plane, I only had to
calculate points for the first quadrant then change the sign of the
`[x, y]` coordinates for each of the other quadrants.  To calculate the
coordinates for each point, I imagined tesselating the rooms in a grid.
Odd-numbered rooms will be mirrored and the new coordinate in one of
these rooms will be the dimension of the room minus the original coordinate.

```text
         0
         |
         | r=0   r=1   r=2   r=3
         |
         |...X. .X... ...X. .X...
         |..... ..... ..... .....  r=1
         |.O... ...O. .O... ...O.
         |..... ..... ..... .....
         |
         |..... ..... ..... .....
         |.O... ...O. .O... ...O.  r=0
         |..... ..... ..... .....
         |...X. .X... ...X. .X...
         +-----------------------------0
```

I kept a running dictionary of hits indexed by the bearing, and skipped
those that already had a shorter distance (as the beam would've collided
with that target first.)  To keep from using two dicts, I "flagged" the
hero's distances by storing them as a negative number -- that way I
could still use them to compare (using `abs()`), but was able to filter
them from the final count.

I originally intended to replace `atan2()` with a function to return a
vector of integers between the two points, but the code I wrote for that
wasn't as obvious so I decided to stay with the trig function.

<details><summary>description</summary>

> Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny
> trainers! Fortunately, you grabbed a beam weapon from an abandoned
> storeroom while you were running through the station, so you have
> a chance to fight your way out. But the beam weapon is potentially
> dangerous to you as well as to the bunny trainers: its beams reflect off
> walls, meaning you'll have to be very careful where you shoot to avoid
> bouncing a shot toward yourself!
>
> Luckily, the beams can only travel a certain maximum distance before
> becoming too weak to cause damage. You also know that if a beam hits
> a corner, it will bounce back in exactly the same direction. And of
> course, if the beam hits either you or the bunny trainer, it will stop
> immediately (albeit painfully).
>
> Write a function solution(dimensions, your_position, trainer_position,
> distance) that gives an array of 2 integers of the width and height of
> the room, an array of 2 integers of your x and y coordinates in the
> room, an array of 2 integers of the trainer's x and y coordinates in the
> room, and returns an integer of the number of distinct directions that
> you can fire to hit the elite trainer, given the maximum distance that
> the beam can travel.
>
> The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <=
> 1250]. You and the elite trainer are both positioned on the integer
> lattice at different distinct positions (x, y) inside the room such that
> [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the
> beam can travel before becoming harmless will be given as an integer 1 <
> distance <= 10000.
>
> For example, if you and the elite trainer were positioned in a room
> with dimensions [3, 2], your_position [1, 1], trainer_position [2, 1],
> and a maximum shot distance of 4, you could shoot in seven different
> directions to hit the elite trainer (given as vector bearings from your
> location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3,
> -2]. As specific examples, the shot at bearing [1, 0] is the straight
> line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces
> off the left wall and then the bottom wall before hitting the elite
> trainer with a total shot distance of sqrt(13), and the shot at bearing
> [1, 2] bounces off just the top wall before hitting the elite trainer
> with a total shot distance of sqrt(5).

</details>

<details open><summary>solution</summary>

```python

from itertools import product
from math import atan2


def solution(dimensions, your_position, trainer_position, distance):
    x0, y0 = your_position
    hits = dict()
    for position in your_position, trainer_position:
        for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, position, reflect, quadrant)
                ]
                travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
                bearing = atan2(x0 - x, y0 - y)
                if travel > distance or bearing in hits and travel > abs(hits[bearing]):
                    continue
                # mark self-hits with a negative travel so we can filter later
                hits[bearing] = travel * (-1 if position == your_position else 1)
    return len([1 for travel in hits.values() if travel > 0])

```

</details>

### Level 5

#### Challenge 5.1 "Dodge the Lasers!"

I first implemented the basic algorithm, but as the description
indicates, "just using sqrt(2) and a loop won't work."
I had no idea what approach the challenge writers were
intending, but my first search taught me that it was a [Beatty
Sequence](https://en.wikipedia.org/wiki/Beatty_sequence).
Further investigation turned up this [Mathematics Stack Exchange
question][beatty].  Between those two resources, I was able to
understand the math enough to write a recursive function (again!)
to solve the problem.

The next difficulty was precision.  Coming from perl I was pleased to
learn how well thought-out python's high-precision floats and large
numbers work.  A small change adjusting the precision of the Decimal
object let the final tests pass.

[beatty]: https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

<details><summary>description</summary>

> Oh no! You've managed to escape Commander Lambda's collapsing space
> station in an escape pod with the rescued bunny workers - but Commander
> Lambda isn't about to let you get away that easily. Lambda sent an elite
> fighter pilot squadron after you -- and they've opened fire!
>
> Fortunately, you know something important about the ships trying to
> shoot you down. Back when you were still Lambda's assistant, the
> Commander asked you to help program the aiming mechanisms for the
> starfighters. They undergo rigorous testing procedures, but you were
> still able to slip in a subtle bug. The software works as a time step
> simulation: if it is tracking a target that is accelerating away at
> 45 degrees, the software will consider the targets acceleration to
> be equal to the square root of 2, adding the calculated result to
> the targets end velocity at each timestep. However, thanks to your
> bug, instead of storing the result with proper precision, it will be
> truncated to an integer before adding the new velocity to your current
> position.  This means that instead of having your correct position, the
> targeting software will erringly report your position as sum(i=1..n,
> floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas
> testing, but enough that it might just save your life.
>
> If you can quickly calculate the target of the starfighters' laser beams
> to know how far off they'll be, you can trick them into shooting an
> asteroid, releasing dust, and concealing the rest of your escape.  Write
> a function solution(str_n) which, given the string representation of an
> integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) +
> ... + floor(n*sqrt(2))) as a string. That is, for every number i in the
> range 1 to n, it adds up all of the integer portions of i*sqrt(2).
>
> For example, if str_n was "5", the solution would be calculated as
>
> ```python
> floor(1*sqrt(2)) +
> floor(2*sqrt(2)) +
> floor(3*sqrt(2)) +
> floor(4*sqrt(2)) +
> floor(5*sqrt(2))
> = 1+2+4+5+7 = 19
> ```
>
> so the function would return "19".
>
> str_n will be a positive integer between 1 and 10^100, inclusive. Since
> n can be very large (up to 101 digits!), using just sqrt(2) and a loop
> won't work. Sometimes, it's easier to take a step back and concentrate
> not on what you have in front of you, but on what you don't.

</details>

<details open><summary>solution</summary>

```python

from decimal import *


def S(a, n):
    if n == 0:
        return 0
    np = int((a - 1) * n)
    return n * np + n * (n + 1) / 2 - np * (np + 1) / 2 - S(a, np)


def solution(s):
    getcontext().prec = 101
    return str(S(Decimal(2).sqrt(), int(s)))

```

</details>

### Complete

#### "For Your Eyes Only"

Upon completion, of level 5, I received a final challenge.

> You've completed all the levels!!
>
> &lt;encrypted>
> EUYAGg1NCRIFSElfSkYUHQtPGEZaT04GBQ0fCg9JGQRRT1NFTQQAGwtLAQQSSEVFTQQVCQFcGBJR T1NFTQgdDBxLCAgUAwxCRkFUDg1GBQQACgQABBVUT1QOSxQYAwYGAQQXSEIOSxMXDQsMHhJUT1QO SxIXCQxCRkFUCQFBS0FMT04SAw9SSBM= &lt;/encrypted>
>
> For your eyes only!

I noticed the `=` at the end of the string, and guessed it was
padding for a base64-encoded string.  It did decode, but it still
wasn't readable text; presumably (as it says) encrypted.  They
didn't give much to go on, so I tried some simple things like
[ROT13](https://en.wikipedia.org/wiki/ROT13) first.  Then I noticed the
"For your eyes only!" and thought that might be the key for something
like an [XOR cipher](https://en.wikipedia.org/wiki/XOR_cipher).  It
wasn't, but the resulting text looked much closer to readable text so I
felt I was on the right track.  Eventually, I guessed it was my Google
username.

<details open><summary>solution</summary>

```python

#!/usr/bin/env python3

from base64 import b64decode
from getpass import getpass
from itertools import cycle

message = """
EUYAGg1NCRIFSElfSkYUHQtPGEZaT04GBQ0fCg9JGQRRT1NFTQQAGwtLAQQSSEVFTQQVCQFcGBJR
T1NFTQgdDBxLCAgUAwxCRkFUDg1GBQQACgQABBVUT1QOSxQYAwYGAQQXSEIOSxMXDQsMHhJUT1QO
SxIXCQxCRkFUCQFBS0FMT04SAw9SSBM=
"""

key = getpass()
for m, k in zip(b64decode(message), cycle(key)):
    print(chr(m ^ ord(k)), end="")
print()

```

```shell
$ ./decrypt.py
Password:
{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}
```

</details>

#### More to come

There was an opportunity at the end to provide my email address so
I could be notified if any new challenges were added in the future.
If I ever receive such a notice, I'll update my progress here.
