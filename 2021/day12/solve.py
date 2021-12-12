from _shared_python.aoc import *
from pprint import pprint
from copy import copy
#------------------------------------------------------------------------------#

def count_paths(edges, n, path, part2 = False, double = False):

    if re.match(r"[a-z]+", n) and n in path:
        if not part2 or double:
            return 0
        else:
            if n == "start" or n == "end":
                return 0

            double = True

    path = copy(path)
    path.append(n)

    if n == "end":
        return 1

    count = 0;

    for nxt in edges[n]:
        count += count_paths(edges, nxt, path, part2, double)

    return count

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split_to_tuple(INPUT, r"(?P<start>[a-zA-Z]+)-(?P<end>[a-zA-Z]+)")

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

edges = dict()

for start, end in INPUT:
    if start in edges:
        if end not in edges[start]:
            edges[start].append(end)
    else:
        edges[start] = [end]

    if end in edges:
        if start not in edges[end]:
            edges[end].append(start)
    else:
        edges[end] = [start]

output1 = count_paths(edges, "start", [])
output2 = count_paths(edges, "start", [], part2 = True, double = False)

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))