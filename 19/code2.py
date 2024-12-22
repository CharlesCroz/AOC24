import sys

def read_data(file):
    towels = None
    patterns = []
    with open(file, 'r') as fp:
        lines = fp.readlines()
        towels = lines[0].strip().split(", ")
        for line in lines[2:]:
            patterns.append(line.strip())
    return towels, patterns

def recipes(towels, pattern):
    if pattern == "":
        return [[]]
    s = []
    for towel in towels:
        if pattern[0:len(towel)] == towel:
            remains = recipes(towels, pattern[len(towel):])
            for remain in remains:
                s.append([towel] + remain.copy())
    return s

towels, patterns = read_data(sys.argv[1])
towels_tree = []
print(f"{len(towels)=}")
for towel in towels:
    tmp = recipes(towels, towel)
    tmp.remove([towel])
    towels_tree.append((towel, tmp, len(tmp) + 1))

towels_tree.sort(key=lambda x:len(x[0]))

for towel in towels_tree:
    print(f"{towel[0]=}")
# print(f"{patterns=}")

# r = 0
# # can_be_done(towels, patterns[0])
# for pattern in patterns:
#     t = can_be_done(towels, pattern)
#     print(f"can_be_done(towels, pattern)={t}")
#     r += t

# print(f"{r=}")
