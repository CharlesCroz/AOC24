import sys
import functools

def read_data(file):
    towels = None
    patterns = []
    with open(file, 'r') as fp:
        lines = fp.readlines()
        towels = lines[0].strip().split(", ")
        for line in lines[2:]:
            patterns.append(line.strip())
    return tuple(towels), patterns

towels, patterns = read_data(sys.argv[1])

longest_towel = len(towels[0])
print(f"{towels}")

@functools.cache
def count_recipes(pattern):
    if len(pattern) == 0:
        return 1
    if len(pattern) == 1:
        for towel in towels:
            if pattern == towel:
                return 1
        return 0
    
    res = 0
    midpoint = len(pattern) // 2
    # Compute overlaps
    for towel in towels:
        l = len(towel)
        if l == 1:
            continue
        for i in range(max(0, midpoint - l + 1), midpoint):
            if pattern[i:i+l] == towel:
                res += count_recipes(pattern[0:i]) * count_recipes(pattern[i+l:])

    res += count_recipes(pattern[0:midpoint]) * count_recipes(pattern[midpoint:])
    return res

r = 0
for pattern in patterns:
    t = count_recipes(pattern)
    print(f"{pattern}\t{t}")
    r += t
print(f"{r=}")
print(f"{count_recipes.cache_info()}")