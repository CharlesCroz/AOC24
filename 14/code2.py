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
sec = 0
# sec = 6285
while True:
    world = []
    for _ in range(size[0]):
         world.append([0] * size[1])
    for machine in machines:
        x = (machine[0][0] + sec * machine[1][0]) % size[0]
        y = (machine[0][1] + sec * machine[1][1]) % size[1]
        world[x][y] += 1
    for j in range(len(world[0])):
        for i in range(len(world)):
            if world[i][j] == 0:
                print(" ", end="")
            else:
                print("x", end="")
        print("")
    if input(f"{sec=}").strip() == "q":
        break
    sec+= 1
