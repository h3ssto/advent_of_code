from _shared_python.aoc import *
from copy import copy

#------------------------------------------------------------------------------#

SEGMENT_MAPPING = [
            [0,1,2,4,5,6],  # 0
            [2,5],          # 1
            [0,2,3,4,6],    # 2
            [0,2,3,5,6],    # 3
            [1,2,3,5],      # 4
            [0,1,3,5,6],    # 5
            [0,1,3,4,5,6],  # 6
            [0,2,5],        # 7
            list(range(7)), # 8
            [0,1,2,3,5,6]   # 9
        ]

def restrict(candidates, indices, values):
    """ Restrict the fields with index in indices to the values in values, 
        remove the values from the other fields"""
    
    for i, cand in enumerate(candidates):
        if i in indices:
            candidates[i] = sorted([x for x in cand if x in values])
        else:
            candidates[i] = sorted([x for x in cand if x not in values])

    return candidates

def common_by_length(length):
    """ Return the common active segments of numbers with length active segments"""
    fields = [i for i, field in enumerate(SEGMENT_MAPPING) 
        if len(field) == length]

    common = SEGMENT_MAPPING[fields[0]]
    for i in fields[1:]:
        common = [x for x in common if x in SEGMENT_MAPPING[i]]

    return common

def verify_all(candidates, n, values):
    """ Verify that candidates appear for all of the common segments, remove otherwise """

    indices = common_by_length(n)

    for i in indices:
        candidates[i] = [x for x in candidates[i] if x in values]

def create_mapping(candidates):
    """ Create the mapping to decode the outputs """

    mapping = dict()

    for i, l in enumerate(SEGMENT_MAPPING):
        key = [candidates[j][0] for j in l]
        key = sorted(key)
        mapping["".join(key)] = i

    return mapping

def decode(x, mapping):
    x = "".join(sorted(list(x)))
    return mapping[x]

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r"\s+[|]\s+")
INPUT = [map_split(line, r"\s+") for line in INPUT]

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

outputs = [out for _,out in INPUT]
output_lengths = [[len(x) for x in out] for out in outputs] 
output_lengths = sorted(sum(output_lengths, []))

part1_targets = [2,4,3,7]
output1 = sum([1 for x in output_lengths if x in part1_targets])

# Part 2
for patterns, outputs in INPUT:
    candidates = [["a","b","c","d","e","f","g"]] * 7

    for pattern in patterns:
        l = len(pattern)
        pl = list(pattern)
        
        if l == 2:
            restrict(candidates, SEGMENT_MAPPING[1], pl)
        elif l == 3:
            restrict(candidates, SEGMENT_MAPPING[7], pl)
        elif l == 4:
            restrict(candidates, SEGMENT_MAPPING[4], pl)
        else:
            verify_all(candidates, l, pl)

        for i,cand in enumerate(candidates):
            if len(cand) == 1:
                restrict(candidates, [i], cand)

    mapping = create_mapping(candidates)

    value = 0
    for out in outputs:
        value = 10 * value + decode(out, mapping)

    output2 += value

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))