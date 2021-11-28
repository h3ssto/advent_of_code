from _shared_python.aoc import *
from copy import copy

#------------------------------------------------------------------------------#

def run(inst):
    executions = [0] * len(inst)
    i = 0

    acc = 0

    while i < len(inst) and executions[i] == 0:
        executions[i] += 1
        cmd, value = inst[i]

        if cmd == "nop":
            i += 1
        elif cmd == "acc":
            acc += value
            i += 1
        elif cmd == "jmp":
            i += value

    if i >= len(inst):
        return True, acc
    else:
        return False, acc

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r"\s+")
INPUT = entries_as_tuples(INPUT, types = (str, int))
#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

# Part 1

_, output1 = run(INPUT)


# Part 2
for i in range(len(INPUT)):
    
    cmd, val = INPUT[i]
    inst = copy(INPUT)

    if cmd == "nop":
        inst[i] = ("jmp", val)
    elif cmd == "jmp":
        inst[i] = ("nop", val)
    else:
        continue

    ret, val = run(inst)

    if ret:
        output2 = val
        break

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))