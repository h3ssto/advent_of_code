from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split_to_tuple(INPUT, r"(?P<cmd>\w)(?P<val>\d+)", (str, int))

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

position_x1 = 0
position_y1 = 0
waypoint_x1 = 1
waypoint_y1 = 0

position_x2 = 0
position_y2 = 0
waypoint_x2 = 10
waypoint_y2 = 1

for cmd, value in INPUT:

    if cmd == "N":
        position_y1 += value
        waypoint_y2 += value
    elif cmd == "E":
        position_x1 += value
        waypoint_x2 += value
    elif cmd == "S":
        position_y1 -= value
        waypoint_y2 -= value
    elif cmd == "W":
        position_x1 -= value
        waypoint_x2 -= value

    elif cmd == "L" or cmd == "R":

        if cmd == "R":
            value = 360 - value

        for i in range(int(value / 90)):
            h = waypoint_x1
            waypoint_x1 = -waypoint_y1
            waypoint_y1 = h

            h = waypoint_x2
            waypoint_x2 = -waypoint_y2
            waypoint_y2 = waypoint_y2
            waypoint_y2 = h
    elif cmd == "F":
        position_x1 += value*waypoint_x1
        position_y1 += value*waypoint_y1
        position_x2 += value*waypoint_x2;
        position_y2 += value*waypoint_y2;

output1 = abs(position_x1) + abs(position_y1)
output2 = abs(position_x2) + abs(position_y2)

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))