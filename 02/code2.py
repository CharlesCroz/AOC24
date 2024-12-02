def process_list(s):
    d = 1 if s[1] >= s[0] else -1
    for a,b in zip(s[0:-1], s[1:]):
        x = (b-a) * d
        if x <= 0 or x > 3:
            return 0
    return 1


with open("./data0", 'r') as fp:
    r = 0
    for line in fp.readlines():
        s = [int(a) for a in line.split(' ')]
        x = process_list(s)
        if x == 1:
            r+=1
        else:
            for i in range(len(s)):
                s2 = s.copy()
                s2.pop(i)
                y = process_list(s2)
                if y == 1:
                    r+=1
                    break
    print(f"{r=}")