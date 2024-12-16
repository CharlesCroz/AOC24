import re
import numpy as np

def read_data():
    world = []
    cmds = ""
    robot = [0, 0]
    with open("./data0", 'r') as fp:
        step = 1
        i = 0
        for line in fp.readlines():
            if line.strip() == "":
                step = 2
            elif step == 1:
                if '@' in line:
                    robot[0] = i
                    robot[1] = line.index('@') * 2
                row = []
                for c in line.strip():
                    if c == '@':
                        row.append('@')
                        row.append('.')
                    elif c == 'O':
                        row.append('[')
                        row.append(']')
                    else:
                        row.append(c)
                        row.append(c)
                world.append(row)
                i += 1
            else:
                cmds += line.strip()
    return world, cmds, robot

def cmd_to_vec(c):
    if c == '^':
        return (-1, 0)
    elif c == 'v':
        return (+1, 0)
    elif c == '<':
        return (0, -1)
    elif c == '>':
        return (0, +1)

def is_free(world, pos):
    return world[pos[0]][pos[1]] == '.'

def can_move_vertically(world, pos, cmd):
    if not cmd in ['^', 'v']:
        return False
    x, y = (pos[0], pos[1])
    dx, _ = cmd_to_vec(cmd)
    if world[x][y] == "[":
        return (is_free(world, [x + dx, y]) \
            or can_move_vertically(world, [x + dx, y], cmd)) \
            and (is_free(world, [x + dx, y + 1]) \
            or can_move_vertically(world, [x + dx, y + 1], cmd))
    elif world[x][y] == "]":
        return (is_free(world, [x + dx, y]) \
            or can_move_vertically(world, [x + dx, y], cmd)) \
            and (is_free(world, [x + dx, y - 1]) \
            or can_move_vertically(world, [x + dx, y - 1], cmd))
    elif world[x][y] == '.':
        return True
    else:
        return False
    
def move_vertically(world, pos, cmd):
    dx, _ = cmd_to_vec(cmd)
    if world[pos[0]][pos[1]] == "[":
        move_vertically(world, [pos[0] + dx, pos[1]], cmd)
        move_vertically(world, [pos[0] + dx, pos[1] + 1], cmd)
        world[pos[0] + dx][pos[1]] = "["
        world[pos[0] + dx][pos[1] + 1] = "]"
        world[pos[0]][pos[1]] = "."
        world[pos[0]][pos[1] + 1] = "."
    elif world[pos[0]][pos[1]] == "]":
        move_vertically(world, [pos[0] + dx, pos[1]], cmd)
        move_vertically(world, [pos[0] + dx, pos[1] - 1], cmd)
        world[pos[0] + dx][pos[1]] = "]"
        world[pos[0] + dx][pos[1] - 1] = "["
        world[pos[0]][pos[1]] = "."
        world[pos[0]][pos[1] - 1] = "."

world, cmds, robot = read_data()

for cmd in cmds:
    dx, dy = cmd_to_vec(cmd)
    # print(f"{cmd=}", end="")
    # if input().strip() == 'q':
    #     break
    if cmd in ['<', '>']:
        x, y = (robot[0], robot[1] + dy)
        while world[x][y] not in ['.', '#']:
            y += dy
        if world[x][y] == '.':
            while y != robot[1]:
                world[x][y] = world[x][y - dy]
                y -= dy
            world[x][y] = '.'
            robot[1] += dy
    elif can_move_vertically(world, [robot[0] + dx, robot[1]], cmd):
        move_vertically(world, [robot[0] + dx, robot[1]], cmd)
        world[robot[0] + dx][robot[1]] = '@'
        world[robot[0]][robot[1]] = '.'
        robot[0] += dx

# for row in world:
#     for c in row:
#         print(f"{c}", end="")
#     print("")

r = 0
for i in range(len(world)):
    for j in range(len(world[0])):
        if world[i][j] == '[':
            r += 100 * i + j

print(f"{r=}")
