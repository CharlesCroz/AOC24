def read_data():
    regs = {}
    prog = []
    with open("./data1", 'r') as fp:
        lines = fp.readlines()
        print(f"{lines=}")
        regs['A'] = int(lines[0].strip().split(": ")[1])
        regs['B'] = int(lines[1].strip().split(": ")[1])
        regs['C'] = int(lines[2].strip().split(": ")[1])
        mem = [int(x) for x in lines[4].strip().split(': ')[1].split(',')]

    return regs, mem

def combo(regs, operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return regs['A']
    elif operand == 5:
        return regs['B']
    elif operand == 6:
        return regs['C']
    else:
        raise ValueError

def adv(regs, operand, pc, stdout):
    regs['A'] = regs['A'] // (2 ** combo(regs, operand))
    pc[0] += 2

def bxl(regs, operand, pc, stdout):
    regs['B'] = regs['B'] ^ operand
    pc[0] += 2

def bst(regs, operand, pc, stdout):
    regs['B'] = combo(regs, operand) % 8
    pc[0] += 2

def jnz(regs, operand, pc, stdout):
    if regs['A'] != 0:
        pc[0] = operand
    else:
        pc[0] += 2

def bxc(regs, operand, pc, stdout):
    regs['B'] = regs['B'] ^ regs['C']
    pc[0] += 2

def out(regs, operand, pc, stdout):
    stdout.append(combo(regs, operand) % 8)
    pc[0] += 2

def bdv(regs, operand, pc, stdout):
    regs['B'] = regs['A'] // (2 ** combo(regs, operand))
    pc[0] += 2

def cdv(regs, operand, pc, stdout):
    regs['C'] = regs['A'] // (2 ** combo(regs, operand))
    pc[0] += 2

def getins(code):
    return (adv, bxl, bst, jnz, bxc, out, bdv, cdv)[code]
    

regs, mem = read_data()
print(f"{regs=}")
print(f"{mem=}")
pc = [0]
stdout = []

while pc[0] < len(mem):
    print(f"{pc[0]=} \t{getins(mem[pc[0]]).__name__} \t{mem[pc[0]+1]} \t{regs}")
    getins(mem[pc[0]])(regs, mem[pc[0] + 1], pc, stdout)

for i in stdout:
    print(f"{i}", end=",")
print("")

