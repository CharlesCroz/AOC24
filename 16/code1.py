import re
import numpy as np

# Node [links]

def read_data():
    world = []
    e = [0, 0]
    s = [0, 0]
    with open("./data00", 'r') as fp:
        i = 0
        for line in fp.readlines():
            world.append(line.strip())
            if 'E' in line:
                e[0:2] = [i, line.index('E')]
            if 'S' in line:
                s[0:2] = [i, line.index('S')]
            i += 1
    return world, e, s

def is_node(world, i, j):
    return world[i][j] != '#' and \
        ( \
               (world[i - 1][j] != '#' and world[i][j - 1] != '#') \
            or (world[i - 1][j] != '#' and world[i][j + 1] != '#') \
            or (world[i + 1][j] != '#' and world[i][j - 1] != '#') \
            or (world[i + 1][j] != '#' and world[i][j + 1] != '#') \
        )

def make_graph(world, e_ij, s_ij):
    nodes = []
    e_id = -1
    s_id = -1
    for i in range(1, len(world) - 1):
        for j in range(1, len(world[0]) - 1):
            if is_node(world, i, j):
                if i == e_ij[0] and j == e_ij[1]:
                    e_id = len(nodes)
                if i == s_ij[0] and j == s_ij[1]:
                    s_id = len(nodes)
                nodes.append([i, j])
    return nodes, e_id, s_id

def find_edges(world, nodes):
    edges = {}
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i][0] == nodes[j][0]:
                is_edge = True
                for t in range(nodes[i][1] + 1, nodes[j][1]):
                    if world[nodes[i][0]][t] == '#' or [nodes[i][0], t] in nodes:
                        is_edge = False
                if is_edge:
                    if i in edges.keys():
                        edges[i].append(j)
                    else: 
                        edges[i] = [j]
                    if j in edges.keys():
                        edges[j].append(i)
                    else: 
                        edges[j] = [i]
            if nodes[i][1] == nodes[j][1]:
                is_edge = True
                for t in range(nodes[i][0] + 1, nodes[j][0]):
                    if world[t][nodes[i][1]] == '#' or [t, nodes[i][1]] in nodes:
                        is_edge = False
                if is_edge:
                    if i in edges.keys():
                        edges[i].append(j)
                    else: 
                        edges[i] = [j]
                    if j in edges.keys():
                        edges[j].append(i)
                    else: 
                        edges[j] = [i]
    return edges
                    
world, e_ij, s_ij = read_data()
print(f"{e_ij}")
print(f"{s_ij}")
for l in world:
    for c in l:
        print(f"{c}", end="")
    print("")
nodes, e_id, s_id = make_graph(world, e_ij, s_ij)
for i in range(len(nodes)):
    print(f"{i: 3d} - {nodes[i]}\t", end="")
    if i > 0 and i % 8 == 0:
        print("")
print(f"{e_id=}")
print(f"{s_id=}")
edges = find_edges(world, nodes)
print(f"{edges=}")

r = 0
print(f"{r=}")
