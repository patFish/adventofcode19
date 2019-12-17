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

from typing import List


def manhattendistance(A: List[str], B: List[str]) -> int:
    return None


A1 = ['R8', 'U5', 'L5', 'D3']
B1 = ['U7', 'R6', '4', 'L4']
assert manhattendistance(A1, B1) == None

# with open('day01-Input.txt') as f:
#     masses = [int(line.strip()) for line in f]
#     res = sum(fuel(mass) for mass in masses)

# print(res)
