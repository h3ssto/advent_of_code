from _shared_python.aoc import *

#------------------------------------------------------------------------------#

def normalize(x, low):
    return int(x, 36) - int(low, 36)

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

ls = map_split(INPUT, r"\s")
ls = [(normalize(x, "A"), normalize(y, "X")) for x,y in ls]

for x,y in ls:
    if y - x == 0:
        output1 += 3

    if y - x == 1 or (x == 2 and y == 0):
        output1 += 6

    output1 += y + 1

for x,y in ls:    
    if y == 0:
        z = (x + 3 - 1) % 3
    elif y == 1:
        z = x
        output2 += 3
    elif y == 2:
        z = (x + 1) % 3
        output2 += 6

    output2 += z + 1

# #------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))