def read_data():
    with open("./data0", 'r') as fp:
        return fp.readline().strip()

layout = read_data()
memory = []
is_prog = True
prog_id = 0
for c in layout:
    if is_prog:
        memory.append([prog_id, int(c)])
        prog_id += 1
    else:
        memory.append([-1, int(c)])
    is_prog = not is_prog

prog_index = len(memory) - 1
while prog_index >= 0:
    prog = memory[prog_index].copy()
    if prog[0] != -1: # don't move free space
        space_index = 0
        while space_index < prog_index:
            space = memory[space_index].copy()
            if space[0] == -1 and space[1] >= prog[1]:
                memory[space_index][0] = prog[0]
                memory[space_index][1] = prog[1]
                if space[1] > prog[1]:
                    prog_index += 1
                    memory.insert(space_index + 1, [-1, space[1] - prog[1]])
                memory[prog_index][0] = -1
                if prog_index < len(memory) - 1 and memory[prog_index + 1][0] == -1:
                    memory[prog_index][1] += memory[prog_index + 1][1]
                    memory.pop(prog_index + 1)
                if prog_index > 0 and memory[prog_index - 1][0] == -1:
                    memory[prog_index - 1][1] += memory[prog_index][1]
                    memory.pop(prog_index)
                break
            space_index += 1
    prog_index -= 1

r = 0
memloc = 0
for data in memory:
    if data[0] != -1:
        for i in range(memloc, memloc + data[1]):
            r += i * data[0]
    memloc += data[1]

print(f"{r=}")
