'''
Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. 
However, that fuel also requires fuel, and that fuel requires fuel, and so on. 
Any mass that would require negative fuel should instead be treated as if it requires zero fuel; 
the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the 
scope of this calculation.
example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
'''

from sys import stdin


def fuel(mass: int) -> int:
    return mass//3 - 2


def liftOffFuel(mass: int) -> int:
  fuels = []
  res = (fuel(mass))
  fuels.append(res)
  while(fuel(res) > 0):
    res = fuel(res)
    fuels.append(res)
  return sum(fuels)


assert liftOffFuel(14) == 2
assert liftOffFuel(1969) == 966
assert liftOffFuel(100756) == 50346

with open('day01-Input.txt') as f:
    masses = [int(line.strip()) for line in f]
    res = sum(liftOffFuel(mass) for mass in masses)
print(res)
