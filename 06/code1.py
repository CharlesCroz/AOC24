def read_data():
    world_map = []
    with open("./data00", 'r') as fp:
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


world_map, guard = read_data()
track = []
for x in range(len(world_map)):
    track.append([0] * len(world_map[0]))

while in_map(guard, world_map):
    track[guard[0]][guard[1]] = 1
    nx, ny = next(guard)
    if in_map([nx, ny], world_map) and world_map[nx][ny] == '#':
        guard[2] = turn(guard[2])
    else:
        guard[0] = nx
        guard[1] = ny

r = 0
for l in track:
    r += sum(l)
print(f"{r=}")
