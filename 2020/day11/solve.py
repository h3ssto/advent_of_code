from _shared_python.aoc import *
from copy import copy
#------------------------------------------------------------------------------#

def evaluate(i, x, y, n, m, read):
    posx = (i % n) + x
    posy = int(i / n) + y
    pos = n * posy + posx

    if 0 <= posx < n and 0 <= posy < m:
        if read[pos] == "#":
            return 1

    return 0

#------------------------------------------------------------------------------#

# Example from the task
#
# INPUT = """\
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""

# INPUT = string_to_list(INPUT)

INPUT = input_from_file(__file__)
INPUT = map2(list, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

n = len(INPUT[0])
m = len(INPUT)

read = sum(INPUT, [])

changes = 1

while changes > 0:
    changes = 0

    write = copy(read)

    for i in range(len(read)):

        if read[i] == ".":
            continue

        stress = 0

        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if x == 0 and y == 0:
                    continue

                stress += evaluate(i, x, y, n, m, read)

        if read[i] == "L" and stress == 0:
            write[i] = "#"
            changes += 1
        
        if read[i] == "#" and stress >= 4:
            write[i] = "L"
            changes += 1

    read = write

output1 = sum([1 for x in read if x == "#"])


# Part 2

read = sum(INPUT, [])

changes = 1

while changes > 0:
    changes = 0

    write = copy(read)

    for i in range(len(read)):

        if read[i] == ".":
            continue

        stress = 0

        posx = i % n
        posy = int(i / n)

        diag_starts = [(-1,-1), (-1, 1), (1,-1), (1,1), (0, -1), (0, 1), (-1, 0), (1, 0)]

        for dx,dy in diag_starts:
            
            x = posx + dx
            y = posy + dy

            while 0 <= x < n and 0 <= y < m:
                pos = y * n + x

                if read[pos] == "L":
                    break

                if read[pos] == "#":
                    stress += 1
                    break

                x += dx
                y += dy

        if read[i] == "L" and stress == 0:
            write[i] = "#"
            changes += 1
        
        if read[i] == "#" and stress >= 5:
            write[i] = "L"
            changes += 1

    read = write

output2 = sum([1 for x in read if x == "#"])

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))