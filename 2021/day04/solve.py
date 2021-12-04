from _shared_python.aoc import *
import re
import math

#------------------------------------------------------------------------------#

def check_bingo(square, sequence, n):

    for i in range(n):

        row = square[i*n:(i+1)*n]
        col = square[i::n]

        if all([x in sequence for x in row]):
            return True

        if all([x in sequence for x in col]):
            return True

    return False

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)

sequence = map_split([INPUT[0]], regex=r",")[0]
sequence = map2(int, sequence)

squares = INPUT[2:]
squares = group_contents(squares, "")

p_leading_whitespace = re.compile(r"^\s+")

for i, square in enumerate(squares):
    # remove leading whitespaces
    square = [p_leading_whitespace.sub("", row) for row in square]
    
    # get digits
    square = map_split(square, r"\s+")
    
    # concatenate
    square = sum(square, [])
    
    square = map2(int, square)
    squares[i] = square

#------------------------------------------------------------------------------#

preview_input(sequence)
preview_input(squares)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

n = int(math.sqrt(len(squares[0])))

winning_boards = []

for square in squares:
    for i in range(n, len(sequence)):
        current = sequence[:i]

        if check_bingo(square, current, n):
            marked = [x for x in square if x in current]
            score = current[-1] * (sum(square) - sum(marked))

            if output1 == 0:
                output1 = score

            winning_boards.append((i, score))
            break 
    
winning_boards = sorted(winning_boards, key = lambda x:x[0])
_, output2 = winning_boards[-1]

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))