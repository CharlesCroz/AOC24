def read_data():
    antennas = {}
    dims = [0, 0]
    with open("./data0", 'r') as fp:
        lines = fp.readlines()
        dims[0] = len(lines)
        dims[1] = len(lines[0].strip())
        for i in range(dims[0]):
            line = lines[i]
            for j in range(dims[1]):
                c = line[j]
                if c != '.':
                    if c in antennas.keys():
                        antennas[c].append([i, j])
                    else:
                        antennas[c] = [[i, j]]
    return antennas, dims

antennas, dims = read_data()
print(f"{antennas=}")
print(f"{dims=}")

nodes = []
for i in range(dims[0]):
    nodes.append([0] * dims[1])

for freq in antennas.values():
    print(f"{freq=}")
    for i in range(len(freq)):
        for j in range(i + 1, len(freq)):
            x0, y0, x1, y1  = (freq[i][0], freq[i][1], freq[j][0], freq[j][1])
            dx = x1 - x0
            dy = y1 - y0
            l = 0
            while x0 - l * dx in range(dims[0]) and y0 - l * dy in range(dims[1]):
                nodes[x0 - l * dx][y0 - l * dy] = 1 
                l -= 1
            l = 0
            while x1 + l * dx in range(dims[0]) and y1 + l * dy in range(dims[1]):
                nodes[x1 + l * dx][y1 + l * dy] = 1 
                l -= 1
            
r = 0

for node in nodes:
    print(f"{node=}")
    r+=sum(node)

print(f"{r=}")