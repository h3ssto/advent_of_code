from _shared_python.aoc import *
from pprint import pprint

#------------------------------------------------------------------------------#

input = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

input = string_to_list(input)
input = input_from_file(__file__)

# ------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

preview_input(input)

cycle = 0
x = 1

screen = [[] for _ in range(7)]

for line in input:
    if line == "noop":
        optime = 1
        v = 0
    elif m := re.match(r"addx (?P<val>[-]?\d+)", line):
        optime = 2
        v = int(m["val"])

    for _ in range(optime):
        
        y = cycle // 40        

        if x - 1 <= cycle % 40 <= x + 1:
            screen[y].append("#")
        else:
            screen[y].append(".")
        
        cycle += 1

        if cycle in [20,60, 100,140,180,220]:
            output1 += cycle * x

    x += v

for line in screen:
    print("".join(line))

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))