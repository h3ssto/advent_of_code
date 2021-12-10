from _shared_python.aoc import *

#------------------------------------------------------------------------------#

points1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

points2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

pairs = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

incompletes = []

for line in INPUT:
    stack = []
    corrupted = False

    for x in line:
        if x in ["(", "[", "{", "<"]:
            stack.append(x)

        if x in [")", "]", "}", ">"]:
            start = stack.pop()

            if pairs[start] != x:
                output1 += points1[x]
                corrupted = True
                break

    if not corrupted:
        closing = reversed(stack)
        score = 0
        for x in closing:
            score = 5 * score + points2[x]

        incompletes.append(score)

output2 = sorted(incompletes)[int(len(incompletes) / 2)]

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))