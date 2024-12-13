from functools import lru_cache

def read_data():
    stones = []
    with open("./data0", 'r') as fp:
        for numbers in fp.readline().strip().split(' '):
            stones.append(int(numbers))
    return stones

@lru_cache(maxsize=None)
def count(blink, n):
    if blink == 0:
        return 1
    if n == 0:
        return count(blink - 1, 1)
    s = f"{n}"
    l = len(s)
    if l % 2 == 0:
        return count(blink - 1, int(s[:l//2])) + count(blink -1, int(s[l//2:]))
    return count(blink - 1, n * 2024)


stones = read_data()
print(f"{stones=}")

r = 0
for stone in stones:
    r += count(75, stone)

print(f"{r=}")
