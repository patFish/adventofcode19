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
    nInstr = len(arg)//2
    idx = 0
    for _ in range(nInstr):
        opcode = '0'+str(arg[idx])
        if len(opcode) > 3:
            isV3immediate, isV2immediate, isV1immediate = [
                bool(x) for x in opcode[0:3]]
            opcode = int(opcode[3:])
        else:
            opcode = int(opcode)
        if isProgramStop(opcode):
            break
        elif isAddtion(opcode):
            val1idx, val2idx, resIdx = arg[idx+1], arg[idx+2], arg[idx+3]
            param1 = val1idx if isV1immediate else arg[val1idx]
            param2 = val2idx if isV2immediate else arg[val2idx]
            arg[resIdx] = param1 + param2
            idx += 4
        elif isMultiplication(opcode):
            val1idx, val2idx, resIdx = arg[idx+1], arg[idx+2], arg[idx+3]
            param1 = val1idx if isV1immediate else arg[val1idx]
            param2 = val2idx if isV2immediate else arg[val2idx]
            arg[resIdx] = param1 * param2
            idx += 4
        elif isInput(opcode):
            ''' Special Input Case'''
            valIdx = arg[idx+1]
            specialInput = int(1)
            arg[valIdx] = specialInput
            idx += 2
        elif isOutput(opcode):
            valIdx = arg[idx+1]
            print(arg[valIdx])
            idx += 2
        else:
            raise Exception('no valid opcode')
    return arg


def isProgramStop(opcode):
    return opcode == 99


def isOutput(opcode):
    return opcode == 4


def isInput(opcode):
    return opcode == 3


def isMultiplication(opcode):
    return opcode == 2


def isAddtion(opcode):
    return opcode == 1


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


Intcode = open('5-in.txt').read().split(',')
print(compute(Intcode))
