import sys

def read_data(file):
    cells = []
    with open(file, 'r') as fp:
        for line in fp.readlines():
            values = line.strip().split(",")
            cells.append((int(values[0]), int(values[1])))
    return cells

def gen_world(d):
    world = []
    for i in range(d):
        world.append(["."] * d)
    return world

d = int(sys.argv[2])
cell_drop = int(sys.argv[3])
cells = read_data(sys.argv[1])
world = gen_world(d)

for i,j in cells[0:int(cell_drop)]:
    world[i][j] = '#'

for row in world:
    for c in row:
        print(f"{c}", end="")
    print("")

def in_world(d, i, j):
    return i in range(d) and j in range(d)

scores = []
for i in range(d):
    scores.append([float('inf')] * d)

done = []
for i in range(d):
    done.append([False] * d)

todo = [(0, 0, 0)]
scores[0][0] = 0

while True:
    v, i, j = todo.pop(0)
    if done[i][j]:
        continue
    scores[i][j] = v
    done[i][j] = True
    if (i,j) == (d-1, d-1):
        print(f"{v=}")
        break
    
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if in_world(d, i + di, j + dj) \
                and world[i + di][j + dj] == '.' \
                and not done[i + di][j + dj] \
                and scores[i + di][j + dj] > v + 1:
            todo.append((v + 1, i + di, j + dj)) 
    

