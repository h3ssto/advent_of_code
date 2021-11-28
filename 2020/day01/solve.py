from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = """"""
INPUT = input_from_file(__file__)
INPUT = map2(int, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = ""
output2 = ""

#------------------------------------------------------------------------------#

for i,x in enumerate(INPUT):
    for j,y in enumerate(INPUT[i+1:]):
        for z in INPUT[j:]:
            if y + z == 2020:
                output1 = y * z

            if x + y + z == 2020:
                output2 = x * y * z

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))