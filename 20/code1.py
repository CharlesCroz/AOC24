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

track = [(i0, j0)]
while len(todo) != 0 :
    val, i, j = todo.pop(0)
    for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        if world[i + di][j + dj] != "#" and scores[i + di][j + dj] > val + 1:
            track.append((i + di, j + dj))
            scores[i + di][j + dj] = val + 1
            todo.append((val + 1, i + di, j + dj))

# print(f"{track}")

cheat_d = int(sys.argv[2])
cheat_min = int(sys.argv[3])

cheats = {}
for i in range(len(track)):
    for j in range(i + cheat_min, len(track)):
        xi, yi = track[i]
        xj, yj = track[j]
        dist = abs(xi - xj) + abs(yi - yj)
        gain = j - i - dist
        if dist <= cheat_d and gain >= cheat_min:
            if gain in cheats.keys():
                cheats[gain] += 1
            else:
                cheats[gain] = 1


print(f"{cheats=}")
# k = list(cheats.keys())
# k.sort()
# for kk in k:
#     print(f"{kk=} {cheats[kk]=}")
print(f"{sum(cheats.values())=}")

