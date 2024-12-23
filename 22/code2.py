import sys

def read_data(file):
    secrets = []
    with open(file, 'r') as fp:
        for line in fp.readlines():
            secrets.append(int(line))
    return secrets

diff_count = int(sys.argv[2])
secrets = read_data(sys.argv[1])

def evolve(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

# Calculate each sequences
scores = []
for secret in secrets:
    sequence = [secret % 10]
    for i in range(diff_count):
        secret = evolve(secret)
        sequence.append(secret % 10)
    diffs = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    buys = {}
    for i in range(0, diff_count - 3):
        k = tuple(diffs[i:i+4])
        v = sequence[i + 4]
        if k not in buys.keys():
            buys[k] = v
    scores.append(buys)

possible_diffs = [x for x in range(-9, 10)]
max_bananas = 0
for a in possible_diffs:
    for b in possible_diffs:
        for c in possible_diffs:
            for d in possible_diffs:
                candidates = 0
                key = (a, b, c, d)
                for seller in scores:
                    if key in seller.keys():
                        candidates += seller[key]
                if candidates > max_bananas:
                    print(f"{key=} {candidates=}")
                    max_bananas = candidates
print(f"{max_bananas=}")
