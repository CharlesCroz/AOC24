import sys

def read_data(file):
    edges = {}
    nodes_lit = []
    with open(file, 'r') as fp:
        for line in fp.readlines():
            edge = line.strip().split("-")
            if edge[0] not in nodes_lit:
                nodes_lit.append(edge[0])
            if edge[1] not in nodes_lit:
                nodes_lit.append(edge[1])
            i = nodes_lit.index(edge[0])
            j = nodes_lit.index(edge[1])
            if i in edges.keys():
                edges[i].append(j)
            else:
                edges[i] = [j]
            if j in edges.keys():
                edges[j].append(i)
            else:
                edges[j] = [i]
    return edges, tuple(nodes_lit)

edges, nodes_lit = read_data(sys.argv[1])
nodes = [x for x in range(len(nodes_lit))]
for e in edges.keys():
    edges[e] = tuple(edges[e])

# print(f"{edges=}")
# print(f"{len(nodes)=}")

NEIGHBORS = edges
MIN_SIZE = 3
CLIQUES = []
def bronker_bosch2(clique, candidates, excluded):
    '''Bron–Kerbosch algorithm with pivot'''
    if not candidates and not excluded:
        if len(clique) >= MIN_SIZE:
           CLIQUES.append(clique)
        return
 
    pivot = pick_random(candidates) or pick_random(excluded)
    for v in list(candidates.difference(NEIGHBORS[pivot])):
        new_candidates = candidates.intersection(NEIGHBORS[v])
        new_excluded = excluded.intersection(NEIGHBORS[v])
        bronker_bosch2(clique + [v], new_candidates, new_excluded)
        candidates.remove(v)
        excluded.add(v)


def pick_random(s):
    if s:
        elem = s.pop()
        s.add(elem)
        return elem
    return False

bronker_bosch2([], set(range(len(nodes))), set())

maxl = 0
maxc = []
for clique in CLIQUES:
    if len(clique) > maxl:
        maxl = len(clique)
        maxc = clique

print(f"{maxc=}")
maxc.sort()
code = [nodes_lit[i] for i in maxc]
code.sort()
print(",".join(code))
# # counts = [len(edges[e]) for e in nodes]

# print(f"{min(counts)=}")

# cycles = set({})
# for node in nodes:
#     if node[0] != "t":
#         continue
#     neigbours = []
#     for a, b in edges:
#         if node == a:
#             neigbours.append(b)
#         elif node == b:
#             neigbours.append(a)
#     for i in range(len(neigbours)):
#         for j in range(i + 1, len(neigbours)):
#             if connects(neigbours[i], neigbours[j], edges):
#                 tmp = [node, neigbours[j], neigbours[i]]
#                 tmp.sort()
#                 cycles.add(tuple(tmp))
# print(f"{cycles=}")

# new_cycles = set({})
# for cycle in cycles:
#     # cycle = next(iter(cycles))
#     for node in nodes:
#         if node in cycle:
#             continue
#         fully_connects = True
#         for n in cycle:
#             if not connects(node, n, edges):
#                 fully_connects = False
#         if fully_connects:
#             tmp = list(cycle) + [node]
#             tmp.sort()
#             new_cycles.add(tuple(tmp))

# print(f"{new_cycles=}")
# print(f"{len(new_cycles)=}")
