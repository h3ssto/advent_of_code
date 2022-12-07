from _shared_python.aoc import *

#------------------------------------------------------------------------------#

input = input_from_file(__file__)[0]

#------------------------------------------------------------------------------#

output1 = -1
output2 = -1

#------------------------------------------------------------------------------#

for i in range(len(input)):
    if output1 < 0 and i + 4 <= len(input) and len(set(input[i:i+4])) == 4:
        output1 = i + 4

    if output2 < 0 and i + 14 <= len(input) and len(set(input[i:i+14])) == 14:
        output2 = i + 14

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))