def value(x, y, dx, data):
    if x > 0                        \
        and x < len(data) - 1       \
        and y > 0                   \
        and y < len(data[x]) - 1    \
        and data[x][y] == 'A'       \
        and (                       \
            (data[x+dx][y+1] == 'M' and data[x-dx][y-1] == 'S') \
            or (data[x+dx][y+1] == 'S' and data[x-dx][y-1] == 'M') \
        ):
        return 1
    return 0

with open("./data0", 'r') as fp:
    data = fp.readlines()
    r = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            r += value(x, y, 1, data) * value(x, y, -1, data)
    print(f"{r=}")