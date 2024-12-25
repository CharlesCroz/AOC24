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
def best_sequences(this_from, this_to, this_layer):
    sequences = get_moves(this_from, this_to, arrowpad)
    if this_layer == 0:
        return sequences
    else:
        results = []
        for sequence in sequences:
            sequence = "A" + sequence
            partial_rewritten_sequence = [""]
            # print(f"Rewritting {sequence=}")
            for i in range(len(sequence) - 1):
                tmp = []
                elts = best_sequences(sequence[i], sequence[i+1], this_layer - 1)
                # print(f"\t{(sequence[i], sequence[i+1], this_layer - 1)}")
                # print(f"\t{elts}")
                for x in partial_rewritten_sequence:
                    for y in elts:
                        tmp.append(x + y)
                partial_rewritten_sequence = tmp
            results += partial_rewritten_sequence
        min_len = min(map(len, results))
        return [x for x in results if len(x) == min_len]

for i in range(10):
    for a in "<>^vA":
        for b in "<>^vA":
            t = best_sequences(a, b, i)

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

    l = 2
    new_paths = []
    for path in paths:
        tmp = [""]
        for i in range(len(path) - 1):
            new_tmp = []
            # print(f"{(path[i], path[i+1], l)}")
            t = best_sequences(path[i], path[i+1], l)
            # print(f"{t=}")
            for x in tmp:
                for y in t:
                    new_tmp.append(x + y)
            tmp = new_tmp
        new_paths += tmp
    # print(f"{new_paths}")
    print(min(map(len, new_paths)))

print(f"{r=}")
