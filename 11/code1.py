def read_data():
    stones = []
    with open("./data0", 'r') as fp:
        for numbers in fp.readline().strip().split(' '):
            stones.append(int(numbers))
    return stones

def mutate(n):
    if n == 0:
        return [1]
    s = f"{n}"
    l = len(s)
    if l % 2 == 0:
        return [int(s[:l//2]), int(s[l//2:])]
    return [n * 2024]


stones = read_data()
print(f"{stones=}")

for i in range(25):
    new_stones = []
    for stone in stones:
        new_stones += mutate(stone)
    stones = new_stones

print(f"{len(stones)=}")
