import re
import numpy as np
from math import floor

def read_data():
    regs = {}
    prog = []
    with open("./data1", 'r') as fp:
        lines = fp.readlines()
        print(f"{lines=}")
        regs['A'] = int(re.findall(r'Register A: ([\d]+)', lines[0].strip())[0])
        regs['B'] = int(re.findall(r'Register B: ([\d]+)', lines[1].strip())[0])
        regs['C'] = int(re.findall(r'Register C: ([\d]+)', lines[2].strip())[0])
        mem = []
        for i in lines[4].strip().split(': ')[1].split(','):
            mem.append(int(i))
        for i in range(len(mem)//2):
            prog.append([mem[2 * i], mem[2 * i + 1]])
    return regs, prog

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
    pc[0] += 1

def bxl(regs, operand, pc, stdout):
    regs['B'] = regs['B'] ^ operand
    pc[0] += 1

def bst(regs, operand, pc, stdout):
    regs['B'] = combo(regs, operand) % 8
    pc[0] += 1

def jnz(regs, operand, pc, stdout):
    if regs['A'] != 0:
        pc[0] = operand
    else:
        pc[0] += 1

def bxc(regs, operand, pc, stdout):
    regs['B'] = regs['B'] ^ regs['C']
    pc[0] += 1

def out(regs, operand, pc, stdout):
    stdout.append(combo(regs, operand) % 8)
    pc[0] += 1

def bdv(regs, operand, pc, stdout):
    regs['B'] = regs['A'] // (2 ** combo(regs, operand))
    pc[0] += 1

def cdv(regs, operand, pc, stdout):
    regs['C'] = regs['A'] // (2 ** combo(regs, operand))
    pc[0] += 1

def getins(code):
    return (adv, bxl, bst, jnz, bxc, out, bdv, cdv)[code]
    

regs, prog = read_data()
print(f"{regs=}")
print(f"{prog=}")
pc = [0]
stdout = []

while pc[0] < len(prog):
    print(f"{pc[0]=} \t{getins(prog[pc[0]][0]).__name__} \t{prog[pc[0]][1]} \t{regs}")
    getins(prog[pc[0]][0])(regs, prog[pc[0]][1], pc, stdout)

for i in stdout:
    print(f"{i}", end=",")
print("")

