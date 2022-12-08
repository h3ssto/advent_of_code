from _shared_python.aoc import *
from pprint import pprint
#------------------------------------------------------------------------------#

input = input_from_file(__file__)
input = map_inner2(int, input)

# ------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#


### Part 1
output1 = len(input)*2 + len(input[0])*2 - 4

for i in range(1, len(input[0]) - 1):
    for j in range(1, len(input) - 1):
        h = input[i][j]
        from_left = max(input[i][:j]) < h
        from_right = max(input[i][j+1:]) < h
        from_top = max([input[k][j] for k in range(i)]) < h
        from_bottom = max([input[k][j] for k in range(i + 1, len(input))]) < h

        if any([from_left, from_right, from_bottom, from_top]):
            output1 += 1


### Part 2
for i in range(1, len(input[0]) - 1):
    for j in range(1, len(input) - 1):
        h = input[i][j]

        # left
        vl = 0
        k = j - 1
        while k >= 0:
            vl += 1
            if input[i][k] >= h:
                break
            k -= 1

        # right
        vr = 0
        k = j + 1
        while k < len(input[0]):
            vr += 1 
            if input[i][k] >= h:
                break
            k += 1

        # top
        vt = 0
        k = i - 1
        while k >= 0:
            vt += 1 
            if input[k][j] >= h:
                break
            k -= 1

        # bottom
        vb = 0
        k = i + 1
        while k < len(input):
            vb += 1 
            if input[k][j] >= h:
                break
            k += 1

        output2 = max(output2,vl * vr * vb * vt)

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))