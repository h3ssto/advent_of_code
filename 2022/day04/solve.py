from _shared_python.aoc import *

#------------------------------------------------------------------------------#

input = input_from_file(__file__)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

pairs = []

for line in input:
    m = re.match(r"(?P<xmin>\d+)-(?P<xmax>\d+),(?P<ymin>\d+)-(?P<ymax>\d+)", line)
    pairs.append((int(m["xmin"]),int(m["xmax"]),int(m["ymin"]),int(m["ymax"])))


### Part 1

for xmin, xmax, ymin, ymax in pairs:
    if (xmin <= ymin and ymax <= xmax) or (ymin <= xmin and xmax <= ymax):
        output1 += 1


### Part 2

for xmin, xmax, ymin, ymax in pairs:
    if (xmin <= ymin <= xmax) or (ymin <= xmin <= ymax):
        output2 += 1

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))