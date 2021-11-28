from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r"-|\s+|:\s+")
INPUT = entries_as_tuples(INPUT, types = (int, int, str, str))

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

for l,u,c,s in INPUT:
    s1 = [x for x in s if x == c]

    if l <= len(s1) <= u:
        output1 += 1

    if (s[l-1] == c) != (s[u-1] == c):
        output2 += 1

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))