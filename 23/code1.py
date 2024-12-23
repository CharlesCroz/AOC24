import sys

def read_data(file):
    links = []
    uniques = set()
    with open(file, 'r') as fp:
        for line in fp.readlines():
            link = line.strip().split("-")
            uniques.add(link[0])
            uniques.add(link[1])
            links.append(tuple(link))
    return links, uniques

links, uniques = read_data(sys.argv[1])

# print(f"{links=}")
# print(f"{uniques=}")
def connects(a, b, ls):
    return (a, b) in ls or (b, a) in ls

cycles = set({})
for node in uniques:
    if node[0] != "t":
        continue
    neigbours = []
    for a, b in links:
        if node == a:
            neigbours.append(b)
        elif node == b:
            neigbours.append(a)
    for i in range(len(neigbours)):
        for j in range(i + 1, len(neigbours)):
            if connects(neigbours[i], neigbours[j], links):
                tmp = [node, neigbours[j], neigbours[i]]
                tmp.sort()
                cycles.add(tuple(tmp))

# print(f"{cycles=}")
print(f"{len(cycles)=}")
