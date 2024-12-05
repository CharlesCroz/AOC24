import re

with open("./data0", 'r') as fp:
    r = 0
    for l in fp.readlines():
        for e in re.findall(r'mul\(([\d]{1,3}),([\d]{1,3})\)', l):
            r+=int(e[0])*int(e[1])
    print(f"{r=}")