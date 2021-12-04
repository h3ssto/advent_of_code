from _shared_python.aoc import *
from copy import copy

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map2(list, INPUT)
INPUT = map_inner2(int, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

l = max([len(x) for x in INPUT])

gamma   = 0
epsilon = 0

for i in range(l):

    ones = sum([1 for x in INPUT if x[i] == 1])

    if ones > len(INPUT) / 2:
        gamma = gamma << 1 | 1
        epsilon = epsilon << 1
    else:
        gamma = gamma << 1
        epsilon = epsilon << 1 | 1

output1 = gamma * epsilon


# Part 2

o2_cand  = copy(INPUT)
co2_cand = copy(INPUT)

for i in range(l):

    if len(o2_cand) > 1:
        ones = sum([1 for x in o2_cand if x[i] == 1])

        if ones >= len(o2_cand) / 2:
            o2_cand = [x for x in o2_cand if x[i] == 1]
        else:
            o2_cand = [x for x in o2_cand if x[i] == 0]

    if len(co2_cand) > 1:
        ones = sum([1 for x in co2_cand if x[i] == 1])

        if ones >= len(co2_cand) / 2:
            co2_cand = [x for x in co2_cand if x[i] == 0]
        else:
            co2_cand = [x for x in co2_cand if x[i] == 1]

    if len(o2_cand) == 1 and len(co2_cand) == 1:
        break

o2_cand  = map2(str, o2_cand[0])
co2_cand = map2(str, co2_cand[0])

o2  = int("".join(o2_cand), 2)
co2 = int("".join(co2_cand), 2) 

output2 = o2 * co2

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))