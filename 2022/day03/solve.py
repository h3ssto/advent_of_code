from _shared_python.aoc import *

#------------------------------------------------------------------------------#

# assumes xs,ys to be sorted
def get_same(xs, ys):

    same = set()
    jmin = 0

    for x in xs:
        if x in ys[jmin:]:
            jmin = ys[jmin:].index(x)
            same.add(x)

    return same


def priority(x : str) -> int:

    if ord(x) <= ord("a"):
        return ord(x) - ord("A") + 27
    else:
        return ord(x) - ord("a") + 1

#------------------------------------------------------------------------------#

bags = input_from_file(__file__)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

### Part 1

cbags = [(s[:int(len(s)/2)], s[int(len(s)/2):]) for s in bags]
cbags = [(sorted(xs), sorted(ys)) for xs, ys in cbags]

for xs,ys in cbags:
    same = get_same(xs, ys)

    for x in same:
        # print(x, priority(x))
        output1 += priority(x)


### Part 2

bags = [sorted(xs) for xs in bags]

for i in range(0, len(bags), 3):
    groups = dict()
    for j, xs in enumerate(bags[i:i+3]):
        for k, ys in enumerate(bags[i:i+3]):
            if j <= k:
                break

            same = get_same(xs,ys)

            for x in same:
                group = groups.get(x, set())
                group.add(j)
                group.add(k)
                groups[x] = group

    for k,v in groups.items():
        if len(v) < 3:
            continue
        
        output2 += priority(k)

# #------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))