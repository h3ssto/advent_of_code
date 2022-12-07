from _shared_python.aoc import *

#------------------------------------------------------------------------------#

input = input_from_file(__file__)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

stacks = []
moves  = []

for line in input:
    if "[" in line:
        stacks.append(line)
    if "move" in line:
        m = re.match(r"move (?P<what>\d+) from (?P<from>\d+) to (?P<to>\d+)", line)        
        moves.append((int(m["what"]), int(m["from"]) - 1, int(m["to"]) - 1))


### Part 1

boxes = []

for stack in reversed(stacks):
    i = 0
    while stack:
        box = stack[:3]
        stack = stack[4:]

        if len(boxes) <= i:
            boxes.append([])

        if box != "   ":
            boxes[i].append(box[1])

        i += 1


for n, f, t in moves:
    for _ in range(n):
        box = boxes[f].pop()
        boxes[t].append(box)

output1 = "".join([box[-1] if box else "" for box in boxes])


### Part 2

boxes = []

for stack in reversed(stacks):
    i = 0
    while stack:
        box = stack[:3]
        stack = stack[4:]

        if len(boxes) <= i:
            boxes.append([])

        if box != "   ":
            boxes[i].append(box[1])

        i += 1

for n, f, t in moves:

    boxes[t].extend(boxes[f][len(boxes[f]) -n:])

    for _ in range(n):
        boxes[f].pop()


output2 = "".join([box[-1] if box else "" for box in boxes])


#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))