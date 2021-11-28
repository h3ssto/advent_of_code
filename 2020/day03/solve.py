from _shared_python.aoc import *

#------------------------------------------------------------------------------#

### Example from the task specification ###
INPUT = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
INPUT = string_to_list(INPUT)

### Overwrite w/ real input
INPUT = input_from_file(__file__)

#------------------------------------------------------------------------------#

preview_input(INPUT, False)

#------------------------------------------------------------------------------#

output1 = 0 # <- b/o counting
output2 = 1 # <- b/o multiplication

#------------------------------------------------------------------------------#

for dx, dy in [(1,1), (3,1), (5,1), (7,1), (1,2)]:

    n = 0
    x = 0
    y = dy

    while y < len(INPUT):
        row = INPUT[y]
        x = (x + dx) % len(row)
        
        if row[x] == "#":
            n += 1

        y += dy

    if (dx, dy) == (3,1):
        output1 = n

    output2 *= n

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))