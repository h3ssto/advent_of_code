from _shared_python.aoc import *
import re

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = group_contents(INPUT, r"")


field_ranges    = INPUT[0]
field_ranges    = entries_as_dicts([field_ranges], r":\s+")[0]

p_split_ranges = re.compile(r"\s+or\s+")
p_split_range  = re.compile(r"-")

for k,v in field_ranges.items():
    ranges = p_split_ranges.split(v)
    ranges = [p_split_range.split(x) for x in ranges]
    ranges = map_inner2(int, ranges)

    field_ranges[k] = []

    for l,u in ranges:
        field_ranges[k].append(range(l,u+1))


my_ticket = INPUT[1][1]
my_ticket = split(my_ticket, r",")
my_ticket = map2(int, my_ticket)


tickets   = INPUT[2][1:]
tickets   = map_split(tickets, r",")
tickets   = map_inner2(int, tickets)

#------------------------------------------------------------------------------#

# preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

all_ranges = sum([r for _,r in field_ranges.items()], [])

valid_tickets = []

for ticket in tickets:

    valid = True

    for x in ticket:
        if all([x not in r for r in all_ranges]):
            output1 += x
            valid = False

    if valid:
        valid_tickets.append(ticket)


field_options = [[k for k,_ in field_ranges.items()]] * len(field_ranges)

decided_fields = dict()

while len(decided_fields) < len(field_ranges):

    for i in range(len(field_options)):
        made_invalid = []
        
        for ticket in valid_tickets:
            value = ticket[i]

            for field in field_options[i]:
                if not any([value in r for r in field_ranges[field]]):
                    made_invalid.append(field)

        field_options[i] = [x for x in field_options[i] if x not in made_invalid]
    
        if len(field_options[i]) == 1:
            decided_fields[field_options[i][0]] = i

    for i, options in enumerate(field_options):
        field_options[i] = [x for x in options if x not in decided_fields]

departure_positions = [i for k,i in decided_fields.items() if k.startswith("departure")]
departure_values = [x for i,x in enumerate(my_ticket) if i in departure_positions]

output2 = foldr(lambda x,y: x*y, 1, departure_values)


#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))