def read_data():
    world_map = []
    with open("./data00", 'r') as fp:
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


world_map = read_data()
id_map = [] 
for l in world_map:
    id_map.append([-1] * len(l))

id = 0
for i in range(len(world_map)):
    for j in range(len(world_map[0])):
        if i > 0 and world_map[i][j] == world_map[i-1][j]:
            id_map[i][j] = id_map[i-1][j]
        elif j > 0 and world_map[i][j] == world_map[i][j-1]:
            id_map[i][j] = id_map[i][j-1]
        else:
            id_map[i][j] = id
            id += 1

parcels = {}
for i in range(len(world_map)):
    for j in range(len(world_map[0])):
        id = id_map[i][j]
        if id in parcels.keys():
            parcels[id][0] += 1
        else:
            parcels[id] = [1, 0]
        if i == 0 or id_map[i][j] != id_map[i-1][j]:
            parcels[id][1] += 1
        if j == 0 or id_map[i][j] != id_map[i][j-1]:
            parcels[id][1] += 1
        if i == len(world_map) - 1 or id_map[i][j] != id_map[i+1][j]:
            parcels[id][1] += 1
        if j == len(world_map[0]) - 1 or id_map[i][j] != id_map[i][j+1]:
            parcels[id][1] += 1


r = 0
for k in parcels.keys():
    # print(f"{k} > {parcels[k]}")
    r += parcels[k][0] * parcels[k][1]

print(f"{r=}")
