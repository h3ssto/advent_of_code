from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

### Examples to overwrite input
# INPUT = "0,3,6" # -> 436 | 175594
# INPUT = "2,1,3" # ->  10 |   2578

INPUT = string_to_list(INPUT[0], r",")
INPUT = map2(int, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT, False)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

prev = dict()

for i,x in enumerate(INPUT):
    prev[x] = i + 1

n = len(INPUT)
last = INPUT[-1]

while n < 30000000:
    old_last = last

    if last in prev:
        last = n - prev[last]
    else:
        last = 0

    prev[old_last] = n
    n += 1

    if n == 2020:
        output1 = last

output2 = last

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))