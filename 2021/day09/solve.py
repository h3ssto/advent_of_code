from _shared_python.aoc import *

#------------------------------------------------------------------------------#

def evaluate(y, x, heights):

    values = []
    
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        i = x + dx
        j = y + dy

        if 0 <= j < len(heights) and 0 <= i < len(heights[j]):
            values.append(heights[j][i])

            if heights[y][x] >= heights[j][i]:
                return False, values

    return True, values

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r"")
INPUT = [l[1:-1] for l in INPUT]
INPUT = map_inner2(int, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 1

#------------------------------------------------------------------------------#

lows = []

for y,l in enumerate(INPUT):
    for x, v in enumerate(l):
        
        b, ls = evaluate(y, x, INPUT)

        if b:
            lows.append((x,y,v))

output1 = sum([1 + v for _,_,v in lows])


# Part 2

basins = []

for low in lows:
    basin = [low]

    for (x,y,v) in basin:
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            a = x + dx
            b = y + dy

            if 0 <= b < len(INPUT) and 0 <= a < len(INPUT[b]):
                w = INPUT[b][a]

                if w == 9:
                    continue

                if (a,b,w) in basin:
                    continue

                basin.append((a,b,w))

    basins.append(basin)

basin_sizes = sorted([len(basin) for basin in basins], reverse = True)

for basin_size in basin_sizes[:3]:
    output2 *= basin_size

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))