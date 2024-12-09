def read_data():
    with open("./data0", 'r') as fp:
        return fp.readline().strip()

layout = read_data()
memory = []
is_prog = True
prog_id = 0
for c in layout:
    if is_prog:
        memory += [prog_id] * int(c)
        prog_id += 1
    else:
        memory += [-1] * int(c)
    is_prog = not is_prog

free_space = 0
while free_space < len(memory) - 1:
    if memory[free_space] == -1:
        memory[free_space] = memory.pop()
        while memory[-1] == -1:
            memory.pop()
    free_space += 1

r = 0
for i in range(len(memory)):
    r += i * memory[i]
print(f"{r=}")
