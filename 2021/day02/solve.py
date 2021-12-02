from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r" ")
INPUT = entries_as_tuples(INPUT, types = (str,int))
#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = ""
output2 = ""

#------------------------------------------------------------------------------#

hor = 0
depth1 = 0
depth2 = 0


for c,v in INPUT:
    if c == "down":
        depth1 += v
    elif c == "up":
        depth1 -= v
    else:
        hor += v
        depth2 += v * depth1

output1 = hor * depth1
output2 = hor * depth2

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))