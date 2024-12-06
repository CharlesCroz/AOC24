import copy
from joblib import Parallel, delayed

def read_data():
    world_map = []
    with open("./data0", 'r') as fp:
        data = fp.readlines()

        for x in range(len(data)):
            row = []
            for y in range(len(data[0]) - 1):
                c = data[x][y]
                if c == '#':
                    row.append('#')
                elif c == '.':
                    row.append('.')
                else:
                    row.append('.')
                    guard = [x, y, c]
            world_map.append(row)    
    return world_map, guard

def in_map(guard, world_map):
    if guard[0] < 0 or guard[0] >= len(world_map) or guard[1] < 0 or guard[1] >= len(world_map[0]):
        return False
    else:
        return True 

def next(guard):
    dx, dy = {
        '^':(-1, 0),
        'v':(1,  0),
        '<':(0, -1),
        '>':(0,  1),
    }[guard[2]]
    return guard[0] + dx, guard[1] + dy 

def turn(c):
    return {
        '^':'>',
        'v':'<',
        '<':'^',
        '>':'v'
    }[c]

def loops(world_map, guard): 
    track = []
    for x in range(len(world_map)):
        row = []
        for y in range(len(world_map[0])):
            row.append([])
        track.append(row)

    while in_map(guard, world_map):
        if guard[2] in track[guard[0]][guard[1]]:
            return True
        track[guard[0]][guard[1]].append(guard[2])
        nx, ny = next(guard)
        if in_map([nx, ny], world_map) and world_map[nx][ny] == '#':
            guard[2] = turn(guard[2])
        else:
            guard[0] = nx
            guard[1] = ny
    return False


world_map, guard = read_data()

def process_line(world_map, guard, x):
    r = 0
    for y in range(len(world_map[0])):
        if world_map[x][y] == '#':
            continue
        tmp_map = copy.deepcopy(world_map)
        tmp_map[x][y] = '#'
        if loops(tmp_map, guard.copy()):
            r += 1
    print(f"{(x)=}")
    return r


results = Parallel(n_jobs=8)(delayed(process_line)(world_map, guard, x) for x in range(len(world_map)))

print(f"{results=}")
print(f"{sum(results)=}")