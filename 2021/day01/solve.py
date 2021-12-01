from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map2(int, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = ""
output2 = ""

#------------------------------------------------------------------------------#

output1 = sum([1 for x,y in zip(INPUT, INPUT[1:]) if y > x])

ls = [x+y+z for x,y,z in zip(INPUT, INPUT[1:], INPUT[2:])]
output2 = sum([1 for x,y in zip(ls, ls[1:]) if y > x])

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))