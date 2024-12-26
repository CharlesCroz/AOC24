import sys
from copy import deepcopy
from joblib import Parallel, delayed

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

def print_formula(ops, reg, endline=False):
    if endline:
        print(f"{reg} = ", end="")
    if reg[0] in 'xyz':
        print(reg, end="")
    for op in ops:
        if op[2] == reg:
            print("(", end="")
            print_formula(ops, op[0])
            print(f" {op[3].__name__} ", end="")
            print_formula(ops, op[1])
            print(")", end="")
    if endline:
        print("")


# for i in range(46):
#     print_formula(ops, f"z{i:02}", endline=True)

# print_formula(ops, "hqh", endline=True)

def compute(x, y, ops):
    regs = []

    for i in range(45):
        update(ops, f"x{i:02}", x % 2)
        x //= 2
    for i in range(45):
        update(ops, f"y{i:02}", y % 2)
        y //= 2

    while len(ops) > 0:
        found = False
        for i in range(len(ops)):
            op = ops[i]
            if isinstance(op[0], int) and isinstance(op[1], int):
                reg = op[2]
                val = op[3](op[0], op[1])
                regs.append((reg, val))
                ops.pop(i)
                update(ops, reg, val)
                found = True
                break
        if not found:
            return -1
    
    regs.sort(reverse=True)
    r = 0
    for reg, val in regs:
        if reg[0] == "z":
            r = 2 * r + val
    return r

s = set()
for op in ops:
    s.add(op[2])
candidates = tuple(s)

# print(f"{candidates=}")

def swap(ops, i, j):
    tmp = ops[i][2] 
    ops[i][2] = ops[j][2]
    ops[j][2] = tmp

swap(ops, 155 - 92, 190 - 92)
swap(ops, 244 - 92, 170 - 92)
swap(ops, 297 - 92, 301 - 92)

# x = (2 ** 45) - 1
# x = 0
# for i in range(45):
#     y = 2 ** i - 1
#     z = compute(x, y, deepcopy(ops))
#     print(f"{z:046b}")

# for i in range(len(candidates)):
#     z = compute(x, 123456, swap(ops, target, i))
#     expected_z = x + 123456
#     if z != -1 and  z % 2 ** 30 == expected_z % 2 ** 30:
#         print(f"{(i, ops[target][2], ops[i][2])=} : {z:046b}")

# for k in range(len(candidates)):
def test_k(k, ops):
    x = (2 ** 44) - 1
    for l in range(len(candidates)):
        swapped = deepcopy(ops)
        swap(swapped, k, l)
        is_ok = True
        for y in [0, 1]:
            z = compute(x, y, deepcopy(swapped))
            if z == -1 or x+y != z:
                is_ok = False
                break
        if is_ok:
            print(f"{(k, l)=}")

test_k(186-92, ops)
# results = Parallel(n_jobs=8)(delayed(test_from_k)(k, ops) for k in range(len(candidates)))

def print_formula_2(ops, reg, level=0, max_rec=10):
    if level > max_rec:
        return
    spaces = '| ' * level
    if reg[0] in 'xy':
        return
    for op in ops:
        if op[2] == reg:
            print(f"{spaces}{op[2]} = {op[0]} {op[3].__name__} {op[1]}")
            print_formula_2(ops, op[0], level + 1, max_rec)
            print_formula_2(ops, op[1], level + 1, max_rec)

print_formula_2(ops, sys.argv[3], max_rec=int(sys.argv[2]))