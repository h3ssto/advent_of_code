from _shared_python.aoc import *
from pprint import pprint

#------------------------------------------------------------------------------#

def get_move(move):
    m = re.match(r"(?P<d>\w) (?P<l>\d+)", move)
    d = m["d"]
    l = int(m["l"])

    if d == "L":
        return -1, 0, l
    elif d == "R":        
        return 1, 0, l
    elif d == "U":
        return 0, 1, l
    elif d == "D":
        return 0, -1, l

#------------------------------------------------------------------------------#

input = input_from_file(__file__)

# ------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

preview_input(input)

pos = []
pos2 = set()
pos9 = set()

for _ in range(10):
    pos.append((0,0))

for move in input:
    dx, dy, l = get_move(move)

    for _ in range(l):

        hx, hy = pos[0]
        pos[0] = hx + dx, hy + dy

        for i in range(len(pos) - 1):
            hx, hy = pos[i]
            tx, ty = pos[i + 1]

            if abs(hx - tx) == 0:
                if abs(hy - ty) > 1:
                    ty += (hy - ty) // abs(hy - ty)
            elif abs(hy - ty) == 0:
                if abs(hx - tx) > 1:
                    tx += (hx - tx) // abs(hx - tx)
            elif abs(hx - tx) + abs(hy - ty) > 2: 
                tx += (hx - tx) // abs(hx - tx)
                ty += (hy - ty) // abs(hy - ty)

            pos[i] = (hx, hy)
            pos[i+1] = (tx, ty)

        pos2.add(pos[1])
        pos9.add(pos[-1])

output1 = len(pos2)
output2 = len(pos9)

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))