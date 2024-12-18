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
n_incr = int(sys.argv[4])
cells = read_data(sys.argv[1])
world = gen_world(d)

for i, j in cells[0:cell_drop]:
    world[i][j] = '#'

def in_world(d, i, j):
    return i in range(d) and j in range(d)

n = cell_drop
while True:
    for _ in range(n_incr):
        x, y = cells[n]
        world[x][y] = '#'
        n += 1
    todo = [(0, 0, 0)]
    done = []
    for i in range(d):
        done.append([False] * d)

    while True:
        if len(todo) == 0:
            for row in world:
                for c in row:
                    print(f"{c}", end="")
                print("")
            print(f"{n=} {cells[n-1]=}")
            exit(0)
        v, i, j = todo.pop(0)
        if done[i][j]:
            continue
        done[i][j] = True
        if (i,j) == (d-1, d-1):
            print(f"{v=}")
            break
        
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if in_world(d, i + di, j + dj) \
                    and world[i + di][j + dj] == '.' \
                    and not done[i + di][j + dj]:
                todo.append((v + 1, i + di, j + dj)) 
    

