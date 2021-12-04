from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r" ")
INPUT = entries_as_tuples(INPUT, types = (str,int))

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

hor = 0    # same for both parts
depth1 = 0 # same calculation as aim -> use for part 2
depth2 = 0

for cmd, value in INPUT:
    if cmd == "down":
        depth1 += value
    elif cmd == "up":
        depth1 -= value
    else:
        hor += value
        depth2 += value * depth1

output1 = hor * depth1
output2 = hor * depth2

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))