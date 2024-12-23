import sys

def read_data(file):
    secrets = []
    with open(file, 'r') as fp:
        for line in fp.readlines():
            secrets.append(int(line))
    return secrets

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

r = 0
for secret in secrets:
    for i in range(2000):
        secret = evolve(secret)
    r += secret
print(f"{r=}")
