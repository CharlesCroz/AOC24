import re

with open("./data0", 'r') as fp:
    t = fp.read()
    segments = t.split("do()")
    r = 0
    for segment in segments:
        l = segment.split("don't()")[0]
        for e in re.findall(r'mul\(([\d]{1,3}),([\d]{1,3})\)', l):
            r+=int(e[0])*int(e[1])
    print(f"{r=}")