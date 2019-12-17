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

from typing import List, Tuple


def crossedWires(A: List[str], B: List[str]) -> int:
    # transform Lists,
    aP = transform2Points(A)
    bP = transform2Points(B)
    # find matching Points
    poi = matchingPoints(aP, bP)
    print(poi)
    # get shortest distance
    pass


def transform2Points(A: List[str]) -> List[Tuple[int]]:
    res = []
    currentPoint = (0, 0)
    point = List
    for instr in A:
        direction = instr[:1]
        distance = int(instr[1:])
        if direction == 'R':
            point = (currentPoint[0]+distance, currentPoint[1])
        elif direction == 'L':
            point = (currentPoint[0]-distance, currentPoint[1])
        elif direction == 'U':
            point = (currentPoint[0], currentPoint[1]+distance)
        elif direction == 'D':
            point = (currentPoint[0], currentPoint[1]-distance)
        else:
            raise Exception('no valid direction')
        currentPoint = point
        res.append(point)
    print(res)
    return res


def matchingPoints(A: List[Tuple[int]], B: List[Tuple[int]]) -> List[Tuple[int]]:
    res = []
    for p1 in A:
        if B.count(p1) > 0:
            res.append(p1)
    return res


def mannhattenDistance(A: Tuple[int]) -> int:
    return A[0] + A[1]


one = {
    'A': ['R8', 'U5', 'L5', 'D3'],
    'B': ['U7', 'R6', 'D4', 'L4'],
    'MD': 6
}
# assert crossedWires(one['A'], one['B']) == one['MD']
two = {
    'A': ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    'B': ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
    'MD': 159
}
# assert crossedWires(two['A'], two['B']) == two['MD']
three = {
    'A': ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
    'B': ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'],
    'MD': 135
}
# assert crossedWires(three['A'], three['B']) == three['MD']

# with open('day01-Input.txt') as f:
#     masses = [int(line.strip()) for line in f]
#     res = sum(fuel(mass) for mass in masses)

# print(res)

print(crossedWires(one['A'], one['B']))
