def read_data():
    world_map = []
    heads = []
    with open("./data0", 'r') as fp:
        i = 0
        for line in fp.readlines():
            l = line.strip()
            numbers = []
            for j in range(len(l)):
                numbers.append(int(l[j]))
                if numbers[-1] == 0:
                    heads.append([i, j])
            world_map.append(numbers)
            i += 1
    dims = [len(world_map), len(world_map[0])]
    return world_map, heads, dims

def neighbours(pos, dims):
    result = []
    if pos[0] > 0:
        result.append([pos[0] - 1, pos[1]])
    if pos[0] < dims[0] - 1:
        result.append([pos[0] + 1, pos[1]])
    if pos[1] > 0:
        result.append([pos[0], pos[1] - 1])
    if pos[1] < dims[1] - 1:
        result.append([pos[0], pos[1] + 1])
    return result

def find_ends(pos, world_map, dims):
    local_value = world_map[pos[0]][pos[1]]
    if local_value == 9:
        return [pos.copy()]
    result = []
    for n in neighbours(pos, dims):
        if world_map[n[0]][n[1]] == (local_value + 1):
            new_ends = find_ends(n, world_map, dims)
            for ne in new_ends:
                if ne not in result:
                    result.append(ne.copy())
    return result

world_map, heads, dims = read_data()
for l in world_map:
    print(f"{l=}")
print(f"{heads=}")
print(f"{dims=}")

r = 0
for h in heads:
    tmp = find_ends(h, world_map, dims) 
    r += len(tmp)
print(f"{r=}")
