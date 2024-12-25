import sys

def read_thing(lines):
    thing = [0] * 5
    for line in lines:
        for i in range(5):
            if line[i] == "#":
                thing[i] += 1
    return tuple(thing)

def read_data(file):
    keys = []
    locks = []
    with open(file) as fp:
        lines = fp.readlines()
    for i in range(0, len(lines), 8):
        if lines[i].strip() == '#####':
            locks.append(read_thing(lines[i+1:i+6]))
        else:
            keys.append(read_thing(lines[i+1:i+6]))
            
    return keys, locks

keys, locks = read_data(sys.argv[1])

# print(f"{locks=}")
# print(f"{keys=}")

def compatible(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True

r = 0
for key in keys:
    for lock in locks:
        if compatible(key, lock):
            r += 1
print(f"{r=}")