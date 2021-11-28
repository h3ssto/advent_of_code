from _shared_python.aoc import *
from copy import copy

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map2(int, INPUT)
INPUT = sorted(INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

diffs = [0,0,0]

# Diff to outlet
diffs[INPUT[0] - 1] = 1

# Diff to device
diffs[2] = 1

for i in range(1, len(INPUT)):
    diffs[INPUT[i] - INPUT[i-1] - 1] += 1

output1 = diffs[0] * diffs[2]


# Part 2

ls = []

# Prepend the outlet
INPUT.insert(0,0)

# For all adapters get list of connectable smaller adapters
for i, y in enumerate(INPUT):

    left = [x for x in INPUT[:i] if x < y and y - x <= 3]
    ls.append((y, left))

visits = [0] * (INPUT[-1] + 1)

for pos, l in ls:
    if l:
        visits[pos] = max(1, sum([max(1, visits[y]) for y in l]))     

output2 = visits[-1]

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))