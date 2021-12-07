from _shared_python.aoc import *

#------------------------------------------------------------------------------#

positions = input_from_file(__file__)
positions = map_split(positions, r",")[0]
positions = map2(int, positions)

positions = sorted(positions)

#------------------------------------------------------------------------------#

preview_input(positions)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

med = positions[int(len(positions)/2)]
avg_l = int((sum(positions) / len(positions)))

output1 = sum([abs(x-med) for x in positions])
output2 = min([sum([sum(list(range(1, abs(avg-x) + 1)))    
    for x in positions]) for avg in [avg_l, avg_l +1]])

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))