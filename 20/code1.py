import sys
from copy import deepcopy

def read_data(file):
    world = []
    with open(file, 'r') as fp:
        i = 0
        for line in fp.readlines():
            row = []
            for c in line.strip():
                row.append(c)
            world.append(row)
            if 'E' in line:
                e = (i, line.index('E'))
            if 'S' in line:
                s = (i, line.index('S'))
            i += 1
    return world, e, s

world, (i0, j0), (ix, jx) = read_data(sys.argv[1])

scores = []
for row in world:
    scores.append([float('inf')] * len(row))
todo = [(0, i0, j0)]
scores[i0][j0] = 0

while len(todo) != 0 :
    val, i, j = todo.pop(0)
    for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        if world[i + di][j + dj] != "#" and scores[i + di][j + dj] > val + 1:
            scores[i + di][j + dj] = val + 1
            todo.append((val + 1, i + di, j + dj))

def diamond(r, i, j, imax, jmax):
    result = []
    for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        x = i + r * di
        y = j + r * dj
        if x in range(imax) and y in range(jmax):
            result.append((x, y))
    return result

cheats = {}
for i in range(1, len(world) - 1):
    for j in range(1, len(world[0]) - 1):
        if scores[i][j] == float('inf'):
            continue
        for r in [2]:
            candidates = diamond(r, i, j, len(world), len(world[0]))
            for x, y in candidates:
                if scores[x][y] == float('inf'):
                    continue
                diff = scores[x][y] - scores[i][j] - r
                if diff > int(sys.argv[2]):
                    if diff in cheats.keys():
                        cheats[diff] += 1
                    else:
                        cheats[diff] = 1

# print(f"{cheats=}")
k = list(cheats.keys())
k.sort()
for kk in k:
    print(f"{kk=} {cheats[kk]=}")
print(f"{sum(cheats)=}")

# # for row in scores:
#     for c in row:
#         print(f"{c:4}", end="")
#     print("")
