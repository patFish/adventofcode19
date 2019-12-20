'''
Stepping forward 4 more positions arrives at opcode 99, halting the program.

Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
'''
from typing import List


def compute(arg: List[int]) -> List[int]:
    nInstr = (len(arg)//4) if len(arg) % 4 == 0 else (len(arg)//4+1)
    for k in range(nInstr):
        idx = k*4
        opcode = '0'+str(arg[idx])
        if len(opcode) > 2:
            mode3, mode2, mode1 = [int(x) for x in opcode]
            opcode = int(opcode[3:])
        else:
            opcode = int(opcode)
        if opcode == 99:
            break
        elif opcode == 1:
            val1idx, val2idx, resIdx = arg[idx+1], arg[idx+2], arg[idx+3]
            if mode2 == 1:
                arg[resIdx] = arg[val1idx] + arg[val2idx]
            elif mode1 == 1:
                arg[resIdx] = arg[val1idx] + arg[val2idx]
        elif opcode == 2:
            val1idx, val2idx, resIdx = arg[idx+1], arg[idx+2], arg[idx+3]
            arg[resIdx] = arg[val1idx] * arg[val2idx]
        elif opcode == 3:
            ''' Special Input Case'''
            specialInput = int(1)
            arg[val1idx] = specialInput
        elif opcode == 4:
            print(arg[idx+1])
        else:
            raise Exception('no valid opcode')
    return arg


# assert np.array_equal(compute([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
# assert np.array_equal(compute([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])
# assert np.array_equal(compute([2,4,4,5,99,0]), [2,4,4,5,99,9801])
# assert np.array_equal(compute([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])

# with open('day02-Input.txt') as f:
#     instr = f.readline().strip().split(',')
#     for noun in range(99):
#         for verb in range(99):
#             inval = list(map(int, instr))
#             inval[1] = noun
#             inval[2] = verb
#     # print(inval)
#             res = compute(inval)
#             if res[0] == 19690720:
#                 print(noun, verb, res[0])
#                 print(100*noun + verb)
#                 break


# Intcode = open('5-in.txt').read().split(',')
# print(Intcode)
