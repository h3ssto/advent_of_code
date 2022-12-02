from _shared_python.aoc import *

#------------------------------------------------------------------------------#

headers = []

def parse_package(bits):
    header = None
    typeid = None

    sequence = []

    if not bits or int(bits, 2) == 0:
        return "", []

    if 3 <= len(bits):
            header = int(bits[:3],2)
            headers.append(header)
            bits = bits[3:]
    else:
        return bits, sequence

    if 3 <= len(bits):
            typeid = int(bits[:3],2)
            bits = bits[3:]
    else:
        return bits, sequence

    package_end = False
    if typeid == 4:
        while not package_end and bits:
            if bits[0] == "0":
                package_end = True

            bits = bits[1:]

            if 4 <= len(bits):
                data = bits[:4]

                if sequence:
                    sequence[-1] += data
                else:
                    sequence = [data]

                bits = bits[4:]
            else:
                return bits, sequence
    else:
        bits, sequence = parse_operator(bits)

        if typeid == 0:
            sequence = [f"{sum([int(x,2) for x in sequence]):b}"]
        elif typeid == 1:
            value = 1
            for x in sequence:
                x = int(x, 2)
                value *= x

            sequence = [f"{value:b}"]
        elif typeid == 2:
            sequence = [f"{min([int(x,2) for x in sequence]):b}"]
        elif typeid == 3:
            sequence = [f"{max([int(x,2) for x in sequence]):b}"]
        else:

            x = int(sequence[0],2)
            y = int(sequence[1],2)

            if typeid == 5:
                sequence = ["1"] if x > y else ["0"]
            elif typeid == 6:
                 sequence = ["1"] if x < y else ["0"]
            elif typeid == 7:
                sequence = ["1"] if x == y else ["0"]

    return bits, sequence


def parse_operator(bits):
    sequence = []

    if not bits or int(bits, 2) == 0:
        return "", sequence

    if bits[0] == "0":
        length = 15
    else:
        length = 11

    bits = bits[1:]

    if length <= len(bits):
        size = int(bits[:length], 2)
        bits = bits[length:]
    else:
        return bits, sequence

    if length == 15 and size <= len(bits):

        pbits = bits[:size]
        bits = bits[size:]

        while len(pbits) > 0:
            pbits, pseq = parse_package(pbits)
            sequence.extend(pseq)
    else:
        for _ in range(size):
            bits, pseq = parse_package(bits)
            sequence.extend(pseq)

    return bits, sequence

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)[0]

#------------------------------------------------------------------------------#

# preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

bits = "".join([f"{int(x, 16):b}".zfill(4) for x in INPUT])
sequence = []

while bits:
    bits, pseq = parse_package(bits)
    sequence.extend(pseq)

output1 = sum(headers)
output2 = int(sequence[0], 2)

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))