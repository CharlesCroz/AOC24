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

def can_be_done(towels, pattern):
    if pattern == "":
        return True
    for towel in towels:
        # print(f"Testing {towel} vs {pattern}")
        if pattern[0:len(towel)] == towel and can_be_done(towels, pattern[len(towel):]):
            return True
    return False

towels, patterns = read_data(sys.argv[1])

towels.sort(key=len)
for i in range(len(towels),-1,-1):
    if can_be_done(towels[0:-1], towels[-1]):
        towels = towels[0:-1]
    else:
        towels = [towels[-1]] + towels[0:-1]

print(f"{towels=}")
print(f"{patterns=}")

r = 0
# can_be_done(towels, patterns[0])
for pattern in patterns:
    if can_be_done(towels, pattern):
        print(f"{pattern} can be done")
        r+= 1
    else:
        print(f"{pattern} can't be done")

print(f"{r=}")
