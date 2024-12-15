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
                    robot[1] = line.index('@')
                row = []
                for c in line.strip():
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

def test_cmd(world, cmd, pos):
    dx, dy = cmd_to_vec(cmd)
    x, y = pos[0], pos[1]
    while True:
        if world[x][y] == '#':
            return False, None
        elif world[x][y] == '.':
            return True, (x, y)
        x += dx
        y += dy

world, cmds, robot = read_data()

for cmd in cmds:
    dx, dy = cmd_to_vec(cmd)
    can_move, last_cell = test_cmd(world, cmd, robot)

    if can_move:
        if last_cell[0] != robot[0] + dx or last_cell[1] != robot[1] + dy:
            world[last_cell[0]][last_cell[1]] = world[robot[0] + dx][robot[1] + dy]
        world[robot[0]][robot[1]] = '.'
        world[robot[0] + dx][robot[1] + dy] = '@'
        robot[0] += dx
        robot[1] += dy

r = 0
for i in range(len(world)):
    for j in range(len(world[0])):
        if world[i][j] == 'O':
            r += 100 * i + j

print(f"{r=}")
