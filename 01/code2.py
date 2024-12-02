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
    for a in l0:
        r += int(a)*l1.count(a)
    print(f"{r=}")