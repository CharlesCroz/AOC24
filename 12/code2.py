def read_data():
    world_map = []
    with open("./data0", 'r') as fp:
        for line in fp.readlines():
            world_map.append(line.strip())
    return world_map

def mutate(n):
    if n == 0:
        return [1]
    s = f"{n}"
    l = len(s)
    if l % 2 == 0:
        return [int(s[:l//2]), int(s[l//2:])]
    return [n * 2024]

def grow(x, y, ident, world, ids):
    ids[x][y] = ident
    if x > 0 and ids[x-1][y] == -1 and world[x][y] == world[x-1][y]:
        grow(x-1, y, ident, world, ids)
    if y > 0 and ids[x][y-1] == -1 and world[x][y] == world[x][y-1]:
        grow(x, y-1, ident, world, ids)
    if x < len(world) - 1 and ids[x+1][y] == -1 and world[x][y] == world[x+1][y]:
        grow(x+1, y, ident, world, ids)
    if y < len(world[0]) - 1 and ids[x][y+1] == -1 and world[x][y] == world[x][y+1]:
        grow(x, y+1, ident, world, ids)

world_map = read_data()
id_map = [] 
for l in world_map:
    id_map.append([-1] * len(l))

id = 0
for i in range(len(world_map)):
    for j in range(len(world_map[0])):
        if id_map[i][j] == -1:
            grow(i, j, id, world_map, id_map)
            id += 1

def is_out(i, j, world):
    return i < 0 or j < 0 or i > len(world) - 1 or j > len(world[0]) - 1

def is_top_border(i, j, world, id):
    if is_out(i, j, world) or world[i][j] != id:
        return False
    elif is_out(i-1, j, world):
        return True
    else:
        return world[i-1][j] != id

def is_bottom_border(i, j, world, id):
    if is_out(i, j, world) or world[i][j] != id:
        return False
    elif is_out(i+1, j, world):
        return True
    else:
        return world[i+1][j] != id

def is_left_border(i, j, world, id):
    if is_out(i, j, world) or world[i][j] != id:
        return False
    elif is_out(i, j-1, world):
        return True
    else:
        return world[i][j-1] != id

def is_right_border(i, j, world, id):
    if is_out(i, j, world) or world[i][j] != id:
        return False
    elif is_out(i, j+1, world):
        return True
    else:
        return world[i][j+1] != id


parcels = {}
for i in range(len(world_map)):
    for j in range(len(world_map[0])):
        id = id_map[i][j]
        if id in parcels.keys():
            parcels[id][0] += 1
        else:
            parcels[id] = [1, 0, world_map[i][j]]
        if is_top_border(i, j, world_map, world_map[i][j]) and not is_top_border(i, j - 1, world_map, world_map[i][j]):
            parcels[id][1] += 1
        if is_left_border(i, j, world_map, world_map[i][j]) and not is_left_border(i - 1, j, world_map, world_map[i][j]):
            parcels[id][1] += 1
        if is_bottom_border(i, j, world_map, world_map[i][j]) and not is_bottom_border(i, j - 1, world_map, world_map[i][j]):
            parcels[id][1] += 1
        if is_right_border(i, j, world_map, world_map[i][j]) and not is_right_border(i - 1, j, world_map, world_map[i][j]):
            parcels[id][1] += 1


r = 0
for k in parcels.keys():
    print(f"{k} > {parcels[k]}")
    r += parcels[k][0] * parcels[k][1]

print(f"{r=}")
