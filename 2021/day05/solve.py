from _shared_python.aoc import *

#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r"\s+->\s+")
INPUT = [map_split(x, r",") for x in INPUT]
INPUT = [sum(x, []) for x in INPUT]
INPUT = map_inner2(int, INPUT)
INPUT = [((a,b),(x,y)) for a,b,x,y in INPUT]

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

points1 = dict()
points2 = dict()

for (a,b),(x,y) in INPUT:
    diagonal = False

    if a != x and b != y:
        diagonal = True

    if a == x:
        dx = 0
    else:
        dx = int((x - a) / abs(x - a))
    
    if b == y:
        dy = 0
    else:
        dy = int((y - b) / abs(y - b))

    while a != x+dx or b != y+dy:
        if not diagonal:
            points1[(a, b)] = points1.get((a,b), 0) + 1
        
        points2[(a, b)] = points2.get((a,b), 0) + 1
        a += dx
        b += dy

output1 = sum([1 for _, v in points1.items() if v >= 2])
output2 = sum([1 for _, v in points2.items() if v >= 2])

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))