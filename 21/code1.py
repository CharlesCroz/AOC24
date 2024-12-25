import sys
import functools

def read_data(file):
    codes = []
    with open(file, 'r') as fp:
        for line in fp.readlines():
            codes.append(line.strip())
    return codes

codes = read_data(sys.argv[1])
numpad = ("789", "456", "123", " 0A")
arrowpad = (" ^A", "<v>")

@functools.cache
def find_coords(e, pad):
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if pad[i][j] == e:
                return i, j
    raise ValueError

@functools.cache
def get_path(a, b, pad):
    i0, j0 = find_coords(a, pad)
    i1, j1 = find_coords(b, pad)

    di = i1 - i0
    dj = j1 - j0

    if di > 0:
        di_char = di * "v"
    else:
        di_char = (-di) * "^"
    
    if dj > 0:
        dj_char = dj * ">"
    else:
        dj_char = (-dj) * "<"
    
    result = []
    if pad[i1][j0] == " ":
        result.append(dj_char + di_char)
    elif pad[i0][j1] == " ":
        result.append(di_char + dj_char)
    else:
        result.append(di_char + dj_char)
        if di_char + dj_char != dj_char + di_char:
            result.append(dj_char + di_char)
    return result


r = 0
for code in codes:
    print(f"{code=}")
    paths = [""]
    r0_at = "A"
    for c in code:
        new_paths = []
        tmp = get_path(r0_at, c, numpad)
        for deb in paths:
            for end in tmp:
                new_paths.append(deb + end + "A")
        paths = new_paths
        r0_at = c
    # print(f"{paths}")
    # print(f"{len(paths)=}")

    for i in range(2):
        new_paths = []
        for path in paths:
            paths_rx = [""]
            rx_at = "A"
            for c in path:
                new_paths_r1 = []
                tmp = get_path(rx_at, c, arrowpad)
                for deb in paths_rx:
                    for end in tmp:
                        new_paths_r1.append(deb + end + "A")
                paths_rx = new_paths_r1
                rx_at = c
            new_paths += paths_rx
        # print(f"{new_paths}")
        d = min(map(len, new_paths))
        paths = [p for p in new_paths if len(p) == d]
        # print(f"{min(paths, key=len)}")
        # print(f"{len(paths)=}")

    min_value = float('inf')
    for path in paths:
        if len(path) < min_value:
            min_value = len(path)
    print(f"{min_value=}")
    print(f"{int(code[:-1])=}")

    r += min_value * int(code[:-1])

print(f"{r=}")
