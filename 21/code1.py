import sys

def read_data(file):
    codes = []
    with open(file, 'r') as fp:
        for line in fp.readlines():
            codes.append(line.strip())
    return codes

codes = read_data(sys.argv[1])
numpad = ["789", "456", "123", " 0A"]
arrowpad = [" ^A", "<v>"]

def find_coords(e, pad):
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if pad[i][j] == e:
                return i, j
    raise ValueError

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

print(f"{codes=}")

r = 0
for code in codes:
    paths_r0 = [""]
    r0_at = "A"
    for c in code:
        new_paths_r0 = []
        tmp = get_path(r0_at, c, numpad)
        for deb in paths_r0:
            # if len(deb) > 0 and len(tmp) > 1 and deb[-2] == tmp[0]:
            #     new_paths_r0.append(deb + tmp[0] + "A")
            # elif len(deb) > 0 and len(tmp) > 1 and deb[-2] == tmp[1]:
            #     new_paths_r0.append(deb + tmp[1] + "A")
            # else:
            for end in tmp:
                new_paths_r0.append(deb + end + "A")
        paths_r0 = new_paths_r0
        r0_at = c
    print(f"{paths_r0}")

    all_paths_r1 = []
    for path_r0 in paths_r0:
        paths_r1 = [""]
        r1_at = "A"
        for c in path_r0:
            new_paths_r1 = []
            tmp = get_path(r1_at, c, arrowpad)
            for deb in paths_r1:
                for end in tmp:
                    new_paths_r1.append(deb + end + "A")
            paths_r1 = new_paths_r1
            r1_at = c
        all_paths_r1 += paths_r1
    # print(f"{all_paths_r1}")

    all_paths_r2 = []
    for path_r1 in paths_r1:
        paths_r2 = [""]
        r2_at = "A"
        for c in path_r1:
            new_paths_r2 = []
            tmp = get_path(r2_at, c, arrowpad)
            for deb in paths_r2:
                for end in tmp:
                    new_paths_r2.append(deb + end + "A")
            paths_r2 = new_paths_r2
            r2_at = c
        all_paths_r2 += paths_r2
    # print(f"{all_paths_r2}")

    min_value = float('inf')
    for path_r2 in paths_r2:
        if len(path_r2) < min_value:
            min_value = len(path_r2)
    print(f"{min_value=}")
    print(f"{int(code[:-1])=}")

    r += min_value * int(code[:-1])

print(f"{r=}")
