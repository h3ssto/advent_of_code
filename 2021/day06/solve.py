from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r",")[0]
INPUT = map2(int, INPUT)
INPUT = sorted(INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

kinds = [0] * 7

for x in INPUT:
    kinds[x] += 1

n_fish = [sum(kinds)]
nexts = []

for x in range(0,256):

    while len(nexts) > 0 and nexts[0][0] == x:
        _,n = nexts.pop(0)
        kinds[x % 7] += n

    nexts.append((x+9, kinds[x % 7]))

    n_fish.append(sum(kinds) + sum([n for _,n in nexts]))

output1 = n_fish[80]
output2 = n_fish[256]

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))