import sys
import functools

def read_data(file):
    codes = []
    with open(file, 'r') as fp:
        for line in fp.readlines():
            codes.append(line.strip())
    return codes

codes = read_data(sys.argv[1])
numpad = (
    "789",
    "456",
    "123",
    " 0A" )
arrowpad = (
    " ^A", 
    "<v>")

@functools.cache
def find_coords(e, pad):
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if pad[i][j] == e:
                return i, j
    raise ValueError

@functools.cache
def get_moves(a, b, pad):
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
        result.append(dj_char + di_char + "A")
    elif pad[i0][j1] == " ":
        result.append(di_char + dj_char + "A")
    else:
        result.append(di_char + dj_char + "A")
        if di_char + dj_char != dj_char + di_char:
            result.append(dj_char + di_char + "A")
    return result

@functools.cache
def best_lenght(this_from, this_to, this_layer):
    sequences = get_moves(this_from, this_to, arrowpad)
    if this_layer == 0:
        return min(map(len, sequences))
    else:
        results = []
        for sequence in sequences:
            sequence = "A" + sequence
            score = 0
            for i in range(len(sequence) - 1):
                score += best_lenght(sequence[i], sequence[i+1], this_layer - 1)
            results.append(score)
        return min(results)

depth = int(sys.argv[2])

r=0
for code in codes:
    print(f"{code=}")
    paths = ["A"]
    r0_at = "A"
    for c in code:
        new_paths = []
        tmp = get_moves(r0_at, c, numpad)
        for deb in paths:
            for end in tmp:
                new_paths.append(deb + end)
        paths = new_paths
        r0_at = c
    # print(f"{paths}")

    scores = []
    for path in paths:
        # print(f"{path}")
        t = 0
        for i in range(len(path) - 1):
            t += best_lenght(path[i], path[i+1], depth)
            # print(f"{(path[i], path[i+1], t)=}")
        print(f"{path} : {t}")
        scores.append(t)
    r += min(scores) * int(code[:-1])
    # print(f"{min(scores)=}")

print(f"{r=}")
