from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

groups = group_contents(INPUT, "")
groups = map_inner2(int, groups)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

output1 = max([sum(xs) for xs in groups])

groups = sorted(groups, key = lambda x : -sum(x))
output2 = sum([sum(xs) for xs in groups[:3]])

# #------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))