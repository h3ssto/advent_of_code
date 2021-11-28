from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

# Parsing to dict

p_bag_split = re.compile(r"\s+contain\s+")
p_bag_quant = re.compile(r"(?P<quant>\d+)\s+(?P<t>[a-z\s]+)")

p_remove_bag = re.compile(r"\s+bag(s?)")

bags = dict()

for line in INPUT:
    bag, inner_bags = p_bag_split.split(line)

    bag = p_remove_bag.sub("", bag)

    inner_bags = re.split(r",\s+", inner_bags)

    for i, ibag in enumerate(inner_bags):
        m = p_bag_quant.match(ibag)

        if m:
            inner_bags[i] = (int(m["quant"]), p_remove_bag.sub("", m["t"]))
        else:
            inner_bags = []
            break

    bags[bag] = inner_bags


# Part 1

bag_types = []

i = -1

while i < len(bag_types):
    if i < 0:
        bag = "shiny gold"
    else:
        bag = bag_types[i]

    for k,v in bags.items():
        
        if bag in [x for _,x in v]:
            bag_types.append(k)

    i += 1

output1 = len(set(bag_types))


# Part 2

inner_bags = bags["shiny gold"]

i = 0

while i < len(inner_bags):
    q, t = inner_bags[i]

    sub_bags = [(q*x, y) for x, y in bags[t]]
    inner_bags.extend(sub_bags)

    i += 1

output2 = sum([x for x,_ in inner_bags])

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))