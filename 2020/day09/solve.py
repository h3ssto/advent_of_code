from _shared_python.aoc import *
from copy import copy

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map2(int, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

i = 25

while i < len(INPUT):

    n = INPUT[i]

    candidates = INPUT[i-25:i]

    found = False
    for j, x in enumerate(candidates):
        for y in candidates[j+1:]:
            if x + y == n:
                found = True
                break

        if found:
            break

    if not found:
        output1 = n
        break

    i += 1


# Part 2

found = False
for i,x in enumerate(INPUT):

    s = x

    for j,y in enumerate(INPUT[i+1:]):
        s += y

        if s == output1:
            output2 = min(INPUT[i:i+j+2]) + max(INPUT[i:i+j+2])
            found = True
            break

        if s > output1:
            break

    if found:
        break

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))