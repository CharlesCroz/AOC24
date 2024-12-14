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
                np.array([int(elts_x[0][0]) + 10000000000000, int(elts_x[0][1]) + 10000000000000]),
            ])
    return machines

machines = read_data()

r = 0
for i in range(len(machines)):
    machine = machines[i]
    m = np.stack(machine[0:2]).transpose()
    x = np.linalg.solve(m, machine[2]).astype(int)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            a = x[0] + dx 
            b = x[1] + dy 
            if np.array_equal(a * machine[0] + b * machine[1], machine[2]):
                print(f"machine[{i}] contributing {3 * a + b}")
                r += 3 * a + b

print(f"{r=}")
