from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = group_contents(INPUT, sep = "")

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

for group in INPUT:

    for c in range(ord('a'), ord('z') + 1):
        c = chr(c)

        some_yes = False
        all_yes = True

        for p in group:
            if c in p:
                some_yes = True
            else:
                all_yes = False

        if some_yes:
            output1 += 1
            
        if all_yes:
            output2 += 1

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))