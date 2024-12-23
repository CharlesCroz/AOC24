from copy import deepcopy
# Node [links]

def read_data():
    world = []
    e = [0, 0]
    s = [0, 0]
    with open("./data2", 'r') as fp:
        i = 0
        for line in fp.readlines():
            row = []
            for c in line.strip():
                row.append(c)
            world.append(row)
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
            or ([world[i - 1][j], world[i + 1][j], world[i][j - 1], world[i][j + 1]].count("#") == 3) \
        )

def make_graph(world, e_ij, s_ij):
    nodes = []
    edges = {}
    e_id = -1
    s_id = -1
    for i in range(1, len(world) - 1):
        for j in range(1, len(world[0]) - 1):
            if is_node(world, i, j):
                node_id = len(nodes)
                if i == e_ij[0] and j == e_ij[1]:
                    e_id = node_id
                if i == s_ij[0] and j == s_ij[1]:
                    s_id = node_id
                nodes.append([i, j])
                edges[node_id] = []

    for node_id in range(len(nodes)):
        i = nodes[node_id][0]
        j = nodes[node_id][1]
        for ii in range(i - 1, 0, -1):
            if is_node(world, ii, j):
                edges[node_id].append([nodes.index([ii, j]), i - ii, "^"])
                break
            elif world[ii][j] == "#":
                break
        for ii in range(i + 1, len(world) - 1):
            if is_node(world, ii, j):
                edges[node_id].append([nodes.index([ii, j]), ii - i, "v"])
                break
            elif world[ii][j] == "#":
                break
        for jj in range(j - 1, 0, -1):
            if is_node(world, i, jj):
                edges[node_id].append([nodes.index([i, jj]), j - jj, "<"])
                break
            elif world[i][jj] == "#":
                break
        for jj in range(j + 1, len(world[0]) - 1):
            if is_node(world, i, jj):
                edges[node_id].append([nodes.index([i, jj]), jj - j, ">"])
                break
            elif world[i][jj] == "#":
                break

    return nodes, edges, e_id, s_id

def todo_value(t):
    return t[0]

def turn_value(a, b):
    if a == b: # same direction, no cost
        return 0
    elif (a in ["<", ">"] and b in ["<", ">"]) \
        or(a in ["^", "v"] and b in ["^", "v"]): # u-turn
        return -1
    else: # 90 deg turn
        return 1000

world, e_ij, s_ij = read_data()
nodes, edges, e_id, s_id = make_graph(world, e_ij, s_ij)
# for i in range(len(nodes)):
#     print(f"{i=}\t{nodes[i]}")
# for row in world:
#     for c in row:
#         print(f"{c}", end="")
#     print("")


finito = {}
todo = [[0, s_id, ">", [[]]]]
# O : score
# 1 : node_id
# 2 : dir
# 3 : prev ids

while len(todo) != 0 :
    candidate = todo.pop(0)
    # print(f"{candidate=}")
    for edge in edges[candidate[1]]:
        # print(f"{edge=}")
        if (edge[0], edge[2]) in finito.keys():
            continue
        neighbour = nodes[edge[0]]
        t = turn_value(candidate[2], edge[2])
        if t == -1:
            continue
        # print(f"not finito, not uturn")
        new_score = candidate[0] + t + edge[1]
        found = False
        for i in range(len(todo)):
            if todo[i][1] == edge[0] and todo[i][2] == edge[2]:
                found = True
                if  new_score < todo[i][0]:
                    todo[i][0] = new_score
                    todo[i][3] = []
                    for path in candidate[3]:
                        todo[i][3].append(path.copy() + [candidate[1]])
                elif new_score == todo[i][0]:
                    for path in candidate[3]:
                        todo[i][3].append(path.copy() + [candidate[1]])
        if not found:
            todo.append([new_score, edge[0], edge[2], []])
            for path in candidate[3]:
                todo[-1][3].append(path.copy() + [candidate[1]])
            

    finito[(candidate[1], candidate[2])] = (candidate[0], deepcopy(candidate[3]))
    todo.sort(key=todo_value)
    # print(f"{todo=}")
    # print(f"{finito=}")
    # if input().strip() == "q":
        # break

node_ids = [e_id]
print(f"{node_ids=}")


values = [] 
for d in ["<", ">", "^", "v"]:
    if (e_id, d) in finito.keys():
        values.append(finito[(e_id, d)])
print(f"{values=}:{min(values)=}\n{min(values)[1]}")

for path in min(values)[1]:
    path.append(e_id)
    for t in range(len(path) - 1):
        node_a = nodes[path[t]]
        node_b = nodes[path[t + 1]]
        for i in range(min(node_a[0], node_b[0]), max(node_a[0], node_b[0]) + 1):
            for j in range(min(node_a[1], node_b[1]), max(node_a[1], node_b[1]) + 1):
                world[i][j] = "O"


r = 0
for row in world:
    for c in row:
        print(f"{c}", end="")
        if c == 'O':
            r += 1
    print("")
print(f"{r=}")
