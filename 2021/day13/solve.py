from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

points, folds = group_contents(INPUT, "")

points = map_split(points, r",")
points = entries_as_tuples(points, (int,int))

folds  = map_split(folds, r"\s+")
folds  = [fold[-1] for fold in folds]
folds  = map_split_to_tuple(folds, r"(?P<dir>[xy])=(?P<pos>\d+)$", (str, int))

#------------------------------------------------------------------------------#

preview_input(points)
preview_input(folds)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

for i, (dir, pos) in enumerate(folds):
    if dir == "x":
        points = [(min(x, pos - (x - pos)), y) for x,y in points]

    if dir == "y":
        points = [(x, min(y, pos - (y - pos))) for x,y in points]

    points = list(set(points))

    if i == 0:
        output1 = len(points)

points = sorted(points, key = lambda point: (point[1], point[0]))

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2: ", end = "")

curx = 0
cury = 0

for x,y in points:
    for _ in range(cury, y):
        curx = 0
        print()
        print("\t  ", end="")

    for _ in range(curx, x-1):
        print(" ", end = "")

    curx = x
    cury = y
    print(green("#"), end = "")

print()