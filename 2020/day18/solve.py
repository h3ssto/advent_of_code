from _shared_python.aoc import *
from copy import copy

#------------------------------------------------------------------------------#

def eval(ls, base_level = 0):

    print("\neval called with", ls, "at", base_level)

    f = lambda x,y:x+y
    out = 0

    if all([d == base_level for _, d in ls]):
        for x,_ in ls:
            if x == "+":
                f = lambda x,y:x+y
            elif x == "*":
                f = lambda x,y:x*y
            else:
                out = f(out, int(x))

        print("Returning", out, "at", base_level-1)
        return (out, base_level - 1)
    else:

        expr = []
        sub_expr = []
        
        for x,d in ls:
            if d > base_level:
                sub_expr.append((x,d))
            else:
                if sub_expr:
                    expr.append(eval(sub_expr, base_level + 1))
                    sub_expr = []

                expr.append((x,d))

        if sub_expr:
            expr.append(eval(sub_expr, base_level + 1))

        return eval(expr, base_level)



#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
# INPUT = ["1 + (2 * 3) + (4 * (5 + 6))"]
INPUT = map_sub(INPUT, r"[(]", " ( ")
INPUT = map_sub(INPUT, r"[)]", " ) ")
INPUT = map_split(INPUT, r"\s+")

#------------------------------------------------------------------------------#

# preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

results = []

for line in INPUT:
    level = 0

    expr = []

    for i,x in enumerate(line):
        if x == "(":
            level += 1
        elif x == ")":
            level -= 1
        elif x == "":
            pass
        else:        
            expr.append((x, level))

    results.append(eval(expr))

output1 = sum([x for x, _ in results])

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))