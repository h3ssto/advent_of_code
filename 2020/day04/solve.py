from _shared_python.aoc import *

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = group_contents(INPUT, sep = "")
INPUT = map_join(INPUT)
INPUT = map_split(INPUT, regex = r"\s+")
INPUT = entries_as_dicts(INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0 
output2 = 0 

#------------------------------------------------------------------------------#

mandatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

p_4digits = re.compile(r"^\d{4}$")
p_height = re.compile(r"(?P<number>\d+)(?P<unit>(cm|in))")
p_color = re.compile(r"^[#][0-9a-f]{6}$")

ecl_options = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

p_pid = re.compile(r"^[0-9]{9}$")

for entry in INPUT:

    valid = True

    for m in mandatory:
        if m not in entry:
            valid = False
            break

    if not valid:
        continue

    output1 += 1

    for k,v in entry.items():

        if k == "cid":
            continue

        if k not in mandatory:
            valid = False
            break

        if k == "byr":
            if p_4digits.match(v) and 1920 <= int(v) <= 2002:
                continue
            else:
                valid = False
                break

        if k == "iyr":
            if p_4digits.match(v) and 2010 <= int(v) <= 2020:
                continue
            else:
                valid = False
                break

        if k == "eyr":
            if p_4digits.match(v) and 2020 <= int(v) <= 2030:
                continue
            else:
                valid = False
                break

        if k == "hgt":
            m = p_height.match(v)

            if m:
                if m["unit"] == "cm" and 150 <= int(m["number"]) <= 193:
                    continue
                elif m["unit"] == "in" and 59 <= int(m["number"]) <= 76:
                    continue
            
            valid = False
            break

        if k == "hcl":
            if p_color.match(v):
                continue
            else:
                valid = False
                break

        if k == "ecl":
            if v in ecl_options:
                continue
            else:
                valid = False
                break

        if k == "pid":
            if p_pid.match(v):
                continue
            else:
                valid = False
                break

    if valid:
       output2 += 1

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))