'''

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

[R8,U5,L5,D3]
...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
[U7,R6,D4,L4]
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.
'''

from typing import List, Tuple, Dict

dX = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
dY = {'R': 0, 'L': 0, 'U': 1, 'D': -1}


def crossedWires(A: List[str], B: List[str]) -> int:
    # transform Lists,
    aP = transform2Points(A)
    bP = transform2Points(B)
    # combine points
    poi = set(aP.keys())&set(bP.keys())
    # get shortest distance
    return shortesDistance(poi)


def shortesDistance(A: List[Tuple[int]]) -> int:
    return min([abs(x) + abs(y) for (x, y) in A])


def transform2Points(A: List[str]):
    res = {}
    x = 0
    y = 0
    length = 0
    for instr in A:
        direction = instr[0]
        distance = int(instr[1:])
        assert direction in ['R', 'L', 'U', 'D']
        for _ in range(distance):
            x += dX[direction]
            y += dY[direction]
            length += 1
            if (x, y) not in res:
                res[(x, y)] = length
    return res


def matchingPoints(A: List[Tuple[int]], B: List[Tuple[int]]) -> List[Tuple[int]]:
    res = []
    for p1 in A:
        if B.count(p1) > 0:
            res.append(p1)
    return res


def mannhattenDistance(A: Tuple[int]) -> int:
    return abs(A[0]) + abs(A[1])


one = {
    'A': ['R8', 'U5', 'L5', 'D3'],
    'B': ['U7', 'R6', 'D4', 'L4'],
    'MD': 6
}
assert crossedWires(one['A'], one['B']) == one['MD']
two = {
    'A': ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    'B': ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
    'MD': 159
}
assert crossedWires(two['A'], two['B']) == two['MD']
three = {
    'A': ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
    'B': ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'],
    'MD': 135
}
assert crossedWires(three['A'], three['B']) == three['MD']


A, B = open('d03-in.txt').read().split('\n')
A, B = [x.split(',') for x in [A, B]]
res = crossedWires(A, B)
print(res)
