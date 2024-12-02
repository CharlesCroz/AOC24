def process_line(l):
    s = [int(a) for a in l.split(' ')]
    d = 1 if s[1] >= s[0] else -1
    for a,b in zip(s[0:-1], s[1:]):
        x = (b-a) * d
        if x <= 0 or x > 3:
            return 0
    return 1


with open("./data0", 'r') as fp:
    r = 0
    for line in fp.readlines():
        r += process_line(line)
    print(f"{r=}")