from _shared_python.aoc import *

import re

#------------------------------------------------------------------------------#

def step(x, dx, y, dy):

    # print(x, dx, y, dy)
    x += dx
    y += dy

    if dx > 0:
        dx -= 1
    elif dx < 0:
        dx += 1

    dy -= 1

    return x, dx, y, dy


def in_target(x,y,xmin,xmax,ymin,ymax):
    return xmin <= x <= xmax and ymin <= y <= ymax

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)[0]

#------------------------------------------------------------------------------#

output1 = None
output2 = 0

#------------------------------------------------------------------------------#

m = re.match(r"target area: x=(?P<xmin>[-]?\d+)..(?P<xmax>[-]?\d+), y=(?P<ymin>[-]?\d+)..(?P<ymax>[-]?\d+)", INPUT)

xmin = int(m["xmin"])
xmax = int(m["xmax"])
ymin = int(m["ymin"])
ymax = int(m["ymax"])

for dx in range(0, xmax + 1):

    for dy in range(-abs(ymin),abs(ymin)):
        old_dx = dx

        x = 0
        y = 0
        
        positions = []

        for i in range(1000):
            positions.append((x,y))

            if in_target(x, y, xmin, xmax, ymin, ymax):
                max_height = max([y for _,y in positions])
                output1 = max_height if output1 is None or max_height >= output1 else output1
                output2 += 1
                break

            x, dx, y, dy = step(x, dx, y, dy)

            if x > xmax or y < ymin:
                break

        dx = old_dx

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))