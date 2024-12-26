import sys

def XOR(a, b):
    return a ^ b

def OR(a, b):
    return a | b

def AND(a, b):
    return a & b

def read_data(file):
    regs = []
    ops = []
    with open(file) as fp:
        lines = fp.readlines()
    i = 0
    while lines[i].strip() != "":
        t = lines[i].strip().split(": ")
        regs.append((t[0], int(t[1])))
        i += 1
    i += 1
    while i < len(lines):
        t = lines[i].strip().split(" ")
        f = {'XOR':XOR, 'AND':AND, 'OR':OR}[t[1]]
        ops.append([t[0], t[2], t[4], f])
        i += 1
    return regs, ops

regs, ops = read_data(sys.argv[1])

def update(ops, reg, val):
    for op in ops:
        if op[0] == reg:
            op[0] = val
        if op[1] == reg:
            op[1] = val

for reg, val in regs:
    update(ops, reg, val)

while len(ops) > 0:
    for i in range(len(ops)):
        op = ops[i]
        if isinstance(op[0], int) and isinstance(op[1], int):
            reg = op[2]
            val = op[3](op[0], op[1])
            regs.append((reg, val))
            ops.pop(i)
            update(ops, reg, val)
            break

regs.sort(reverse=True)
r = 0
for reg, val in regs:
    if reg[0] == "z":
        print(f"{reg=}\t{val=}")
        r = 2 * r + val
print(f"{r=}")