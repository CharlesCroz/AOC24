import re
import numpy as np

def read_data():
    machines = []
    with open("./data0", 'r') as fp:
        for line in fp.readlines():
            elts = re.findall(r'p=([-]?[\d]*),([-]?[\d]*) v=([-]?[\d]*),([-]?[\d]*)', line.strip())
            machines.append([
                [int(elts[0][0]), int(elts[0][1])],
                [int(elts[0][2]), int(elts[0][3])],
            ])
    return machines

machines = read_data()

size = [101, 103]
quadrants = [0, 0, 0, 0]
for machine in machines:
    x = (machine[0][0] + 100 * machine[1][0]) % size[0]
    y = (machine[0][1] + 100 * machine[1][1]) % size[1]
    if x != (size[0] // 2) and y != (size[1] // 2):
        q = 0
        if x < size[0] // 2:
            q += 1
        if y < size[1] // 2:
            q += 2
        quadrants[q] += 1
    # print(f"{machine=} \tgoes {[x, y]=}")

r = 1
for q in quadrants:
        r *= q
print(f"{r=}")
