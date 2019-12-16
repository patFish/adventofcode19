'''
Stepping forward 4 more positions arrives at opcode 99, halting the program.

Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
'''
from typing import List
import numpy as np


def compute(arg: List[int]) -> List[int]:
    nInstr = (len(arg)//4) if len(arg) % 4 == 0 else (len(arg)//4+1)
    for i in range(nInstr):
        idx = i*4
        opcode = arg[idx]
        if opcode == 99:
            break
        val1idx = arg[idx+1]
        val2idx = arg[idx+2]
        resIdx = arg[idx+3]
        if opcode == 1:
            arg[resIdx] = arg[val1idx] + arg[val2idx]
        elif opcode == 2:
            arg[resIdx] = arg[val1idx] * arg[val2idx]
        else:
            raise Exception('no valid opcode')
        print(arg)
    return arg


assert np.array_equal(compute([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
assert np.array_equal(compute([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])
assert np.array_equal(compute([2,4,4,5,99,0]), [2,4,4,5,99,9801])
assert np.array_equal(compute([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])
