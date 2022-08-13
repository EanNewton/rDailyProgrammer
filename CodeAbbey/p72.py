import sys


def calc(x0, n, a=445, c=700001, m=2097152):
    return [x0:=(a * x0 + c) % m for _ in range(n)]


def p72(raw):
    raw = [_.strip().split() for _ in raw]
    consonants = "bcdfghjklmnprstvwxz"
    vowels = "aeiou"
    seed = int(raw[0][1])
    result = []
    for j, length in enumerate(raw[1]):
        temp = calc(seed, int(length))
        seed = temp[-1]
        result.append("".join([vowels[c%5] if i%2 else consonants[c%19] for i,c in enumerate(temp)]))
    return " ".join(result)


print(p72(sys.stdin.readlines()))