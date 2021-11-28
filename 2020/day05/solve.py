from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

seat_ids = []

for entry in INPUT:
    ver = entry[:7]
    hor = entry[7:]

    ver_l = 0
    ver_u = 127

    hor_l = 0
    hor_u = 7

    for x in ver:
        if x == "F":
            ver_u = int((ver_u + ver_l) / 2)
        else:
            ver_l = int((ver_u + ver_l) / 2) + 1

    for x in hor:
        if x == "L":
            hor_u = int((hor_u + hor_l) / 2)
        else:
            hor_l = int((hor_u + hor_l) / 2) + 1

    seat_id = ver_l * 8 + hor_l
    output1 = max(output1, seat_id)
    seat_ids.append(seat_id)


seat_ids = sorted(seat_ids)

for i in range(0, len(seat_ids) - 1):
    if seat_ids[i] + 2 == seat_ids[i+1]:
        output2 = seat_ids[i] + 1

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))