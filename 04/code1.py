def value(x0, y0, dx, dy, data, word):
    for i in range(len(word)):
        x = x0 + i * dx
        y = y0 + i * dy
        if x < 0 or x >= len(data) or y < 0 or y >= len(data[x]) or data[x][y] != word[i]:
            return 0
    return 1

with open("./data0", 'r') as fp:
    data = fp.readlines()
    r = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    r += value(x, y, dx, dy, data, 'XMAS')
    print(f"{r=}")