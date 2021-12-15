from _shared_python.aoc import *

#------------------------------------------------------------------------------#

def dijkstra(costs, start):
    posx, posy = start

    distances = [[-1]*len(costs[len(costs)-1]) for _ in range(len(costs))]
    distances[posy][posx] = 0

    deltas = [(0,1), (1,0), (-1,0), (0,-1)]
    nexts = [start]

    while nexts:
        posx, posy = nexts.pop(0)
        for dx,dy in deltas:
            x = posx + dx
            y = posy + dy

            if 0 <= y < len(distances) and 0 <= x < len(distances[y]):
                if distances[y][x] == -1:
                    nexts.append((x,y))
                    distances[y][x] = distances[posy][posx] + costs[y][x]
                else:
                    distances[y][x] = min(distances[y][x], distances[posy][posx] + costs[y][x])

        nexts = sorted(nexts, key = lambda x : distances[x[1]][x[0]])

    return distances

#------------------------------------------------------------------------------#

INPUT = input_from_file(__file__)
INPUT = map_split(INPUT, r"")
INPUT = [l[1:-1] for l in INPUT]
INPUT = map_inner2(int, INPUT)

#------------------------------------------------------------------------------#

preview_input(INPUT)

#------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

m = len(INPUT)
n = len(INPUT[m-1])

distances = dijkstra(INPUT, (0,0))
output1 = distances[-1][-1]

map2 = [[0]*n*5 for _ in range(m*5)]
m2 = len(map2)
n2 = len(map2[m2-1])

for i in range(m2):
    for j in range(n2):
        if i < m and j < n:
            map2[i][j] = INPUT[i][j]
        elif i >= j:
            map2[i][j] = max(1, (map2[i-m][j] + 1) % 10)
        else:
            map2[i][j] = max(1, (map2[i][j-n] + 1) % 10)

distances = dijkstra(map2, (0,0))
output2 = distances[-1][-1]

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))