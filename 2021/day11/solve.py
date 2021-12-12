from _shared_python.aoc import *

#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r"")
INPUT = [l[1:-1] for l in INPUT]
INPUT = map_inner2(int, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

for step in range(1, 1000):

    flashing = []

    for y, l in enumerate(INPUT):
        for x, _ in enumerate(l):

            INPUT[y][x] += 1

            if INPUT[y][x] > 9:
                flashing.append((x,y))
                INPUT[y][x] = -1

    for x,y in flashing:
        for dx,dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            a = x + dx
            b = y + dy

            if 0 <= b < len(INPUT) and 0 <= a < len(INPUT[b]):

                cand = INPUT[b][a]

                if cand == -1:
                    continue

                cand += 1

                if cand > 9:
                    flashing.append((a,b))
                    cand = -1

                INPUT[b][a] = cand

    for x,y in flashing:
        INPUT[y][x] = 0

    if step <= 100:
        output1 += len(flashing)

    if len(flashing) == 100:
        output2 = step
        break

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))