import re
import numpy as np

def read_data():
    machines = []
    with open("./data0", 'r') as fp:
        lines = fp.readlines()
        for l in range(0, len(lines), 4):
            elts_a = re.findall(r'X\+([\d]*), Y\+([\d]*)', lines[l + 0].strip())
            elts_b = re.findall(r'X\+([\d]*), Y\+([\d]*)', lines[l + 1].strip())
            elts_x = re.findall(r'X=([\d]*), Y=([\d]*)', lines[l + 2].strip())
            machines.append([
                np.array([int(elts_a[0][0]), int(elts_a[0][1])]),
                np.array([int(elts_b[0][0]), int(elts_b[0][1])]),
                np.array([int(elts_x[0][0]), int(elts_x[0][1])]),
            ])
    return machines

machines = read_data()

r = 0
for machine in machines:
    print(f"{machine}")
    prices = []
    for i in range(100):
        for j in range(100):
            if np.array_equal(i * machine[0] + j * machine[1], machine[2]):
                prices.append(3 * i + j)
    if len(prices) > 0:
        r += min(prices)    

print(f"{r=}")
