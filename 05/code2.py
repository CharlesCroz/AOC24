def read_data():
    rules = {}
    programs = []
    with open("./data0", 'r') as fp:
        lines = fp.readlines()
        l = 0
        while lines[l] != '\n':
            elts = lines[l].split('|')
            lhs = int(elts[0])
            rhs = int(elts[1].strip())
            if lhs in rules.keys():
                rules[lhs].append(rhs)
            else:
                rules[lhs] = [rhs]
            l += 1
        
        l += 1
        for ll in range(l, len(lines)):
            n = []
            for e in lines[ll].strip().split(','):
                n.append(int(e))
            programs.append(n)
    return rules, programs

def fix(program, rules):
    result = program.copy()

    for i in range(len(result)):
        if result[i] in rules.keys():
            for j in range(0, i):
                if result[j] in rules[result[i]]:
                    tmp = result[j]
                    result[j] = result[i]
                    result[i] = tmp
    return result

def valid(program, rules):
    for i in range(len(program)):
        if program[i] in rules.keys():
            for j in range(0, i):
                if program[j] in rules[program[i]]:
                    return False
    return True

rules, programs = read_data()
r = 0
for program in programs:
    if not valid(program, rules):
        fixed = fix(program, rules)
        # print(f"From {program} to {fixed}")
        r += fixed[len(fixed)//2]

# print(f"{rules=}")
# print(f"{programs=}")
print(f"{r=}")
