from _shared_python.aoc import *
import networkx as nx
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------#

def build_graph(input):

    G = nx.DiGraph()

    for i in range(len(input)):
        for j in range(len(input[i])):

            G.add_node((i,j))

            for k, l in [(1, 0), (0, -1), (-1, 0), (0, 1)]:

                k += i
                l += j

                if 0 <= k < len(input) and 0 <= l < len(input[0]):

                    # print((i,j), " to ", (k,l), "is", ord(input[k][l]) - ord(input[i][j]), input[k][l], input[i][j])

                    if ord(input[k][l]) - ord(input[i][j]) <= 1:
                        G.add_edge((i,j), (k,l))
                    elif ord(input[i][j]) - ord(input[k][l]) <= 1:                    
                        G.add_edge((k,l), (i,j))
    return G

#------------------------------------------------------------------------------#

input = input_from_file(__file__)

# ------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

input = [list(line) for line in input]

start = None
end = None

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "S":
            start = (i,j)
            input[i][j] = "a"
        elif input[i][j] == "E":
            end = (i,j)
            input[i][j] = "z"

G = build_graph(input)

path1 = nx.shortest_path(G, start, end)
output1 = len(path1) - 1

output2 = output1

### Part 2
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "a":
            try:
                path2 = nx.shortest_path(G, (i,j), end)

                if len(path2) <= output2:
                    output2 = len(path2) - 1
            except Exception:
                continue

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))