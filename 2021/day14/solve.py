from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

template, rules = group_contents(INPUT, r"")

template = template[0]

rules = map_split_to_tuple(rules, r"(.*)\s+->\s+(.*)", (str, str))

#------------------------------------------------------------------------------#

preview_input(rules)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

pairs = dict()

for x,y in zip(template, template[1:]):
    if (x,y) in pairs:
        pairs[(x,y)] += 1
    else:
        pairs[(x,y)] = 1

for i in range(1,41):

    npairs = dict()
    for (x,y), ins in rules:

        if (x,y) in pairs:
            n = pairs[(x,y)]
        else:
            continue

        npairs[(x,ins)] = npairs.pop((x,ins), 0) + n
        npairs[(ins,y)] = npairs.pop((ins,y), 0) + n
    
    pairs = npairs

    if i == 10 or i == 40:
        counts = []
        for x in set(sum([list(pair) for pair in pairs.keys()], [])):
            count = sum([n for (a,b), n in pairs.items() if a == x])

            if x == template[-1]:
                count += 1

            counts.append((x, count))

        counts = sorted(counts, key = lambda x: x[1])

        if i == 10:
            output1 = counts[-1][1] - counts[0][1]
        else:
            output2 = counts[-1][1] - counts[0][1]

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))