def read_data():
    equations = []
    with open("./data0", 'r') as fp:
        for line in fp.readlines():
            elts = line.split(": ")
            equation = {'res':int(elts[0]), 'vals':[]}
            for val in elts[1].split(' '):
                equation['vals'].append(int(val))
            equations.append(equation)    
    return equations

def solve(target, acc, vals, start):
    if start == len(vals):
        return acc == target
    else:
        return solve(target, acc + vals[start], vals, start + 1) \
            or solve(target, acc * vals[start], vals, start + 1)

equations = read_data()
r = 0

for equation in equations:
    print(f"{equation=}")
    print(f"{solve(equation['res'], equation['vals'][0], equation['vals'], 1)=}")
    if solve(equation['res'], equation['vals'][0], equation['vals'], 1):
        r += equation['res']

print(f"{r=}")
