with open("./data0", 'r') as fp:
    l0 = []
    l1 = []
    for line in fp.readlines():
        t = line.split('   ')
        l0.append(t[0])
        l1.append(t[1].strip())
    l0.sort()
    l1.sort()
    r = 0
    for a,b in zip(l0, l1):
        r += abs(int(a)-int(b))
    print(f"{r=}")