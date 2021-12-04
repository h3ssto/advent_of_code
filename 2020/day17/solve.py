from _shared_python.aoc import *
from copy import copy

#------------------------------------------------------------------------------#

def neighbours(pos, dim = 3):
    x,y,z,w = pos
    l = [-1,0,1]
    
    for dx in l:
        for dy in l:
            for dz in l:
                if dim == 3:                    
                    if any([v != 0 for v in [dx,dy,dz]]):
                        yield (x+dx, y+dy, z+dz, 0)
                else:
                    for dw in l:
                        if any([v != 0 for v in [dx,dy,dz,dw]]):
                            yield (x+dx, y+dy, z+dz, w+dw)


def run(active_cubes, runs = 6, dim = 3, draw = False):

    if draw:
        render(active_cubes, dim)

    for run in range(runs):

        change = dict()

        # Initialize all active_cubes (some )
        for k in active_cubes.keys():
            change[k] = 0

        for pos in active_cubes.keys():
            for k in neighbours(pos, dim = dim):
                change[k] = change.get(k, 0) + 1

        for k, v in change.items():            
            if k in active_cubes:
                if v != 2 and v != 3:
                    active_cubes.pop(k)
            else:
                if v == 3:
                    active_cubes[k] = "#"

        if draw:
            render(active_cubes, dim)
            print("Run", f"#{run + 1},", "active cubes:", len(active_cubes))

    return len(active_cubes)


def render(cubes, dim):

    print(cubes.keys())
    minx = min([k[0] for k in cubes.keys()])
    miny = min([k[1] for k in cubes.keys()])
    minz = min([k[2] for k in cubes.keys()])
    minw = min([k[3] for k in cubes.keys()])

    maxx = max([k[0] for k in cubes.keys()])
    maxy = max([k[1] for k in cubes.keys()])
    maxz = max([k[2] for k in cubes.keys()])
    maxw = max([k[3] for k in cubes.keys()])

    shifty = max(len(str(miny)), len(str(maxy)))
    shiftz = max(len(str(minz)), len(str(maxw)))
    shiftw = max(len(str(minw)), len(str(maxz)))

    for w in range(minw, maxw+1):
        for z in range(minz, maxz+1):
            if dim == 3:
                print(f"z: {z:{shiftz}}")
            else:
                print(f"z: {z:{shiftz}}, w: {w:{shiftw}}")

            for y in range(miny, maxy+1):
                print(f"\ty: {y:{shifty}}", end="\t")
                
                for x in range(minx, maxx+1):
                    if (x,y,z,w) in cubes:
                        print("#", end = "")
                    else:
                        print(".", end = "")

                print()
            print()

    print()

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map2(list,INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

active_cubes = dict()
for y,l in enumerate(INPUT):
    for x,v in enumerate(l):
        if v == "#":
            active_cubes[(x,y,0,0)] = "#"

cubes3 = active_cubes
cubes4 = copy(active_cubes)

output1 = run(cubes3, 6, 3)
output2 = run(cubes4, 6, 4)

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))